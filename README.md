# AWS Cloud SOC – Log Monitoring and Incident Response

**Design and Implementation of a Cloud SOC Environment for Log Monitoring and Incident Response (AWS)**

A cloud-native Security Operations Center (SOC) built using AWS to detect, analyze, and respond to real-time security threats without relying on traditional SIEM solutions.

![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Security](https://img.shields.io/badge/SOC-Detection-blue)
![Status](https://img.shields.io/badge/Project-Completed-green)

---

## Project Overview

This project demonstrates the design and implementation of a cloud-based Security Operations Center (SOC) using AWS native services. The system provides centralized logging, real-time detection, alerting, and incident response across multiple layers of the cloud environment.

---

## Objective

The objective of this project is to build a practical and cost-effective SOC environment in AWS that can:

* Monitor logs from multiple sources
* Detect suspicious activities
* Generate real-time alerts
* Support both automated and manual incident response

---

## Architecture

![AWS SOC Architecture](architecture/aws-cloud-soc-architecture.png)

The architecture follows a structured SOC pipeline where logs from multiple sources are collected, analyzed using CloudWatch, and used to trigger alerts and response actions. Automated responses are handled through AWS Lambda and EventBridge, while manual investigation is performed by the SOC analyst. This design follows a multi-layer security monitoring approach with both automated and manual response capabilities.

---

## Detection and Response Workflow

Attack → Log Collection → Detection (Metric Filters) → Alert (CloudWatch Alarm + SNS) → Response (Lambda / Manual)

---

## AWS Services Used

* Amazon EC2 (SOC Server)
* Amazon VPC (Public Subnet)
* AWS CloudTrail (API activity monitoring)
* VPC Flow Logs (network traffic monitoring)
* Amazon CloudWatch (log monitoring and alarms)
* Amazon SNS (alert notifications)
* AWS Lambda (automated response)
* Amazon EventBridge (event-based trigger)
* Amazon S3 (log storage and archival)
* AWS IAM (access control)

---

## Attack Scenarios Simulated

1. Unauthorized SSH Access
2. SSH Brute Force Attack
3. Port Scanning Attack
4. Security Misconfiguration (Public SSH Access)
5. SYN Flood / DoS Simulation
6. Suspicious API Activity (IAM Privilege Escalation)
7. Data Exfiltration (S3 GetObject)

---

## Log Sources

* CloudTrail → API-level logs
* VPC Flow Logs → Network-level logs
* CloudWatch Agent → OS-level logs (`/var/log/secure`)

---

## Multi-layer Detection

This project implements a multi-layer detection strategy:

* API Layer → AWS CloudTrail
* Network Layer → VPC Flow Logs
* Host Layer → CloudWatch Agent logs

This ensures comprehensive visibility across the cloud environment.

---

## Detection Mechanism

* CloudWatch Log Groups store all logs

* Metric Filters identify suspicious patterns:

  * `REJECT` (blocked traffic)
  * `REJECT AND TCP` (port scanning)
  * `Failed password` (SSH brute force)
  * `AttachUserPolicy` (IAM misuse)
  * `GetObject` (S3 data access)

* CloudWatch Alarms trigger alerts when thresholds are exceeded

---

## Alerting

* Alerts are generated using Amazon SNS
* Notifications are sent via:

  * Email
  * (Optional) SMS or integrations

---

## Automated Response

Automated response is implemented using AWS Lambda and EventBridge to contain threats in real time.

Example actions include:

* Removing insecure SSH rules (`0.0.0.0/0`)
* Blocking malicious IP addresses
* Updating security group configurations

This demonstrates a static automated response approach based on predefined conditions.

---

## Manual Response

Manual incident response actions include:

* Revoking IAM permissions
* Investigating suspicious API activity
* Restricting S3 access
* Performing validation and verification

---

## Incident Response Framework

Incident response follows:

**NIST SP 800-61 (Computer Security Incident Handling Guide)**

Phases:

* Preparation
* Detection & Analysis
* Containment
* Eradication & Recovery
* Post-Incident Activity

---

## Highlights

* Multi-layer detection (API, Network, Host)
* Real-time alerting using CloudWatch and SNS
* Automated response using Lambda and EventBridge
* NIST-based incident response methodology
* Practical simulation of real-world cloud attacks

---

## Sample Detection Evidence

Refer to the `screenshots/` folder for:

* Attack simulation outputs
* CloudWatch alarms
* SNS alert notifications
* Automated response validation

---

## Key Features

* Centralized logging across multiple AWS services
* Real-time detection using CloudWatch
* Alerting using SNS
* Automated response using Lambda
* Support for both automated and manual incident handling

---

## Limitations

* Automated response is static (predefined rules)
* No dynamic attacker identification
* No full SIEM integration

---

## Future Improvements

* Implement dynamic automated response
* Integrate AWS GuardDuty
* Add SIEM tools (Splunk / Microsoft Sentinel)
* Use behavior-based detection
* Implement automated response playbooks

---

## Project Structure

```text
Cloud-SOC-AWS-Capstone/

├── architecture/
├── diagrams/
├── screenshots/
├── lambda-code/
├── commands/
└── report/
```

---

## Author

**Farhana Ahmed**
Cybersecurity Graduate – Centennial College

GitHub: https://github.com/Farhana330/cloud-soc-incident-response-aws
