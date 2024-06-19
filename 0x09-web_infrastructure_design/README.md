# Web Infrastructure Design Project

## Overview

This project involves designing and explaining various web infrastructure setups, covering concepts such as DNS, monitoring, web servers, network basics, load balancers, and servers. The project is divided into tasks, each focusing on a specific aspect of web infrastructure design.

## Team Members

- Wanyoike Mark Edwards

## Project Schedule

- Project Start: Dec 21, 2023, 6:00 AM
- Project End: Jan 2, 2024, 6:00 AM

## Learning Objectives

At the end of this project, you are expected to be able to:

- Explain the components of a web stack.
- Draw a diagram covering the web stack built in the sysadmin/devops track projects.
- Explain the purpose of each component in the infrastructure.
- Understand system redundancy.
- Familiarize yourself with acronyms such as LAMP, SPOF, QPS.

# Tasks

## Single Server Web Infrastructure (www.foobar.com)

### Overview
This document outlines the design and specifications for a one-server web infrastructure hosting the website www.foobar.com. The infrastructure includes a single server with a LAMP stack, comprising a web server (Nginx), an application server, and a MySQL database. The domain www.foobar.com is configured with a www record pointing to the server's IP address (8.8.8.8).

### Components and Roles
1. **Server:**
   - Definition: A physical or virtual machine that hosts the entire web infrastructure.
   - Role: Hosts the web server, application server, and database.

2. **Domain Name:**
   - Role: Serves as a human-readable alias for the server's IP address, allowing users to access the website using www.foobar.com.

3. **Web Server (Nginx):**
   - Role: Handles incoming HTTP requests, serves static content, and forwards dynamic requests to the application server.

4. **Application Server:**
   - Role: Executes the application code and generates dynamic content for client requests.

5. **Database (MySQL):**
   - Role: Stores and retrieves data for the application, ensuring data persistence.

6. **www DNS Record:**
   - Type: CNAME
   - Role: Specifies that www.foobar.com is an alias (canonical name) for the domain's root.

### Issues with Single Server Infrastructure
1. **Single Point of Failure (SPOF):**
   - Risk: If the single server fails, the entire infrastructure becomes unavailable.
   - Mitigation: Consider implementing redundancy or failover mechanisms.

2. **Downtime During Maintenance:**
   - Issue: Restarting the web server for maintenance causes downtime.
   - Mitigation: Implement rolling deployments or use a backup server during maintenance.

3. **Scalability Limitations:**
   - Issue: Unable to handle high traffic as the infrastructure cannot scale horizontally.
   - Mitigation: Consider load balancing and distributed architectures.

## Three Server Web Infrastructure (www.foobar.com)

### Overview
This section expands the infrastructure to three servers, introducing redundancy and scalability through the addition of a load balancer (HAproxy).

### Additional Components and Roles
1. **Load Balancer (HAproxy):**
   - Role: Distributes incoming traffic across multiple servers, improving performance and reliability.

2. **Distribution Algorithm:**
   - Algorithm: Round Robin
   - Explanation: The load balancer distributes requests equally among the available servers, ensuring a balanced load.

3. **Active-Active vs. Active-Passive Setup:**
   - Setup: Active-Active
   - Explanation: All servers actively handle incoming requests, providing high availability and load distribution.

4. **Database Primary-Replica Cluster:**
   - Role: Provides data redundancy and read scalability.
   - Explanation: The primary node accepts write operations, while replica nodes handle read operations.

5. **Primary vs. Replica Nodes:**
   - Application Interaction: The application interacts with the primary node for write operations and replica nodes for read operations.

### Issues with Three Server Infrastructure
1. **Single Points of Failure:**
   - Load Balancer: A single load balancer is a potential SPOF.
   - Mitigation: Consider load balancer redundancy or a high-availability setup.

2. **Security Issues:**
   - Lack of Firewall: Absence of a firewall poses security risks.
   - No HTTPS: Insecure communication jeopardizes data integrity.
   - No Monitoring: Insufficient visibility into system health and performance.

## Secured, Encrypted, and Monitored Three Server Web Infrastructure

### Overview
This section enhances the three-server infrastructure with security measures, SSL encryption, and monitoring components.

### Additional Components and Roles
1. **Firewalls:**
   - Role: Act as barriers between the server and potential threats, filtering incoming and outgoing traffic.

2. **SSL Certificate:**
   - Role: Encrypts traffic between the user and the server, ensuring secure data transmission.

3. **Monitoring Clients (Sumologic):**
   - Role: Collects and analyzes system and application metrics for proactive issue identification.

### Secure and Monitored Infrastructure Specifics
1. **Traffic over HTTPS:**
   - Reason: HTTPS encrypts data in transit, preventing eavesdropping and ensuring data integrity.

2. **Firewalls:**
   - Purpose: Protects against unauthorized access and potential attacks.

3. **Monitoring:**
   - Purpose: Proactively identifies issues, monitors performance, and ensures system health.

4. **Monitoring Tool (Sumologic):**
   - Data Collection: Collects logs and metrics from servers, applications, and databases.
   - Monitoring QPS: Set up custom queries to monitor web server QPS (Queries Per Second).

### Issues with Secured and Monitored Infrastructure
1. **SSL Termination at Load Balancer Level:**
   - Issue: Decrypting SSL at the load balancer exposes traffic within the internal network.
   - Mitigation: Implement end-to-end SSL encryption.

2. **Single MySQL Server for Writes:**
   - Issue: Limits write scalability and poses a potential SPOF.
   - Mitigation: Implement a MySQL cluster for write scalability and redundancy.

3. **Identical Server Components:**
   - Issue: Uniform components across servers pose a risk if a common vulnerability affects all instances simultaneously.
   - Mitigation: Implement diverse configurations and patch management strategies.

## Application Server vs. Web Server

### Overview
This section introduces a cluster configuration for load balancing and redundancy.

### Additional Components and Roles
1. **Load Balancer (HAproxy):**
   - Configuration: Clustered with another load balancer for redundancy.
   - Role: Distributes incoming traffic across multiple servers.

2. **Split Components:**
   - Web Server, Application Server, Database on Separate Servers.

### Clustered Load Balancer Specifics
1. **Clustered Load Balancer:**
   - Reason: Ensures high availability and fault tolerance for load balancing.

2. **Split Components:**
   - Reason: Isolates components for better resource management, scalability, and maintenance.

### Issues with Clustered Load Balancer and Split Components
1. **Load Balancer Cluster:**
   - Issue: Configuration synchronization challenges between load balancer nodes.
   - Mitigation: Implement proper configuration management tools.

2. **Web Server, Application Server, Database Uniformity:**
   - Issue: Identical configurations may lead to simultaneous vulnerabilities.
   - Mitigation: Implement diverse configurations and regular security audits.

## How to Use This Repository

Each task folder contains the whiteboard diagram screenshot and the corresponding GitHub repository link.

## Important Note

- The whiteboard diagrams were presented in front of a mentor, staff, or student without the use of a computer or notes.
- For detailed explanations, refer to the whiteboard sessions and the respective GitHub repositories.

## Copyright

© 2023 ALX. All rights reserved.
