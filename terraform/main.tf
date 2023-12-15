resource "aws_security_group" "jenkins-sg-lab2" {
  name = "jenkins-sg-lab2"
  description = "Security group for Jenkins server"

  ingress {
    description = "Allow SSH access"
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow UI access"
    from_port = 8080
    to_port = 8080
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

}

resource "aws_instance" "jenkins-server" {
    ami = var.ami_id
    instance_type = var.instance_type
    user_data = file("jenkins-userdata.tpl")
    vpc_security_group_ids = [aws_security_group.jenkins-sg-lab2.id]

    tags = {
        Name = "Jenkins-server"
    }
  
}