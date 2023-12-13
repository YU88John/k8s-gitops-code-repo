#!/bin/bash

yum install java -y
wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
yum upgrade -y
yum install jenkins -y
systemctl daemon-reload
systemctl enable jenkins
systemctl start jenkins
yum install git -y
yum install docker -y
usermod -a -G docker ec2-user
usermod -aG docker jenkins
systemctl enable docker.service
systemctl start docker.service


# Note: This userdata is for RHEL-based OS (e.g. Centos, Amazon Linux)


