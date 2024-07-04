# Graduation Prediction System with AWS Autoscaling and Load Testing

This project demonstrates the deployment of a web application with autoscaling on AWS and load testing using Locust. The application predicts the graduation status of students based on their grades.

## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Setting Up AWS Infrastructure](#setting-up-aws-infrastructure)
  - [Launch EC2 Instance](#launch-ec2-instance)
  - [Install Required Software on EC2](#install-required-software-on-ec2)
  - [Deploy Streamlit Application](#deploy-streamlit-application)
- [Setting Up Load Balancer](#setting-up-load-balancer)
  - [Create Target Group](#create-target-group)
  - [Create Load Balancer](#create-load-balancer)
  - [Configure Security Groups](#configure-security-groups)
- [Deploying Locust for Load Testing](#deploying-locust-for-load-testing)
  - [Install Locust](#install-locust)
  - [Run Locust](#run-locust)
  - [Access Locust Web Interface](#access-locust-web-interface)
- [Locust Configuration](#locust-configuration)
- [Monitoring and Autoscaling](#monitoring-and-autoscaling)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project aims to demonstrate the implementation of autoscaling to improve the efficiency and performance of a web application during user traffic spikes. The web application is built using Streamlit and predicts student graduation status based on their grades. Locust is used for load testing.

## Prerequisites

- AWS Account
- SSH Key Pair for EC2
- Basic knowledge of AWS services
- Python and pip installed on your local machine

## Setting Up AWS Infrastructure

### Launch EC2 Instance

1. **Launch an EC2 instance**:
   - AMI: Amazon Linux 2
   - Instance type: t2.micro (Free Tier eligible)
   - Key pair: Select an existing key pair or create a new one
   - Security group: Create a new security group with the following rules:
     - SSH (port 22)
     - HTTP (port 80)
     - Custom TCP (port 8501 for Streamlit)
     - Custom TCP (port 8089 for Locust)

2. **Connect to your EC2 instance**:
   ```sh
   ssh -i "path/to/your-key-pair.pem" ec2-user@your-ec2-public-dns

## Install Required Software on EC2

### Update packages and install dependencies:

```sh
sudo yum update -y
sudo yum install python3 git -y
```

### Install pip and virtualenv:
```sh
sudo python3 -m ensurepip
sudo pip3 install --upgrade pip
sudo pip3 install virtualenv
```

### Clone the project repository:
```sh
git clone https://github.com/your-repo/graduation-prediction-system.git
cd graduation-prediction-system
```

### Set up a virtual environment:
```sh
virtualenv venv
source venv/bin/activate
```

### Install project dependencies:
```sh
pip install -r requirements.txt
```

## Deploy Streamlit Application

### Run the Streamlit app:
```sh
nohup streamlit run app.py --server.port 8501 --server.headless true &
```

### Verify the application:
Access the application at http://your-ec2-public-dns:8501

## Setting Up Load Balancer

### Create Target Group

1. Go to the **EC2 Dashboard**.
2. Under **Load Balancing**, select **Target Groups**.
3. Click on **Create target group**.
4. Select **Instances** as the target type.
5. Configure the target group:
   - **Name**: `uat-target-group`
   - **Protocol**: HTTP
   - **Port**: 8501
   - **VPC**: Select your VPC
6. Click **Create**.

### Create Load Balancer

1. Go to the **EC2 Dashboard**.
2. Under **Load Balancing**, select **Load Balancers**.
3. Click on **Create Load Balancer** and select **Application Load Balancer**.
4. Configure the load balancer:
   - **Name**: `uat-load-balancer`
   - **Scheme**: Internet-facing
   - **Listeners**: HTTP (port 80)
   - **Availability Zones**: Select the same VPC and at least two subnets
5. Click **Next: Configure Security Settings**.
6. Click **Next: Configure Security Groups**, and select your security group.
7. Click **Next: Configure Routing**.
8. Configure the target group:
   - **Target group**: `uat-target-group`
   - **Protocol**: HTTP
   - **Port**: 8501
9. Click **Next: Register Targets**, and add your EC2 instance.
10. Click **Next: Review**, and then **Create**.

### Configure Security Groups

1. Go to the **EC2 Dashboard**.
2. Under **Network & Security**, select **Security Groups**.
3. Select the security group associated with your EC2 instance.
4. Add the following inbound rules:
   - **Type**: HTTP, **Protocol**: TCP, **Port range**: 80, **Source**: 0.0.0.0/0
   - **Type**: Custom TCP, **Protocol**: TCP, **Port range**: 8501, **Source**: 0.0.0.0/0
   - **Type**: Custom TCP, **Protocol**: TCP, **Port range**: 8089, **Source**: 0.0.0.0/0

## Deploying Locust for Load Testing

### Install Locust

1. **Install Locust**:

   ```sh
   pip install locust
   ```

## Run Locust
```sh
nohup locust -f locustfile.py --host http://your-load-balancer-url --web-host 0.0.0.0 &

```

## Access Locust Web Interface

**Access Locust interface**:
- URL: `http://your-ec2-public-dns:8089`
- Configure the number of users and spawn rate, then start the test.

## Locust Configuration

**Configure number of users and spawn rate**:
- **Number of users**: [adjustable]
- **Spawn rate**: [insert the number here] user per second
- **Host**: `http://<load-balancer-url>`

## Monitoring and Autoscaling

- Monitor your application performance using the AWS Management Console.
- Set up CloudWatch Alarms to trigger scaling actions based on metrics like CPU utilization.
- Configure Autoscaling Groups to automatically add or remove instances based on demand.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
