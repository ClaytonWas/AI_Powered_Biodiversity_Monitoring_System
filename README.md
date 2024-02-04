# AI-Powered Biodiversity Monitoring System
![image](https://github.com/ClaytonWas/AI_Powered_Biodiversity_Monitoring_System/assets/60206739/55b66126-8201-4e86-8b83-bf34c795f0fb)

### Table of Contents
- [Overview](#overview)
  - [Use case](#use-case)
  - [Stakeholders](#stakeholders)
- [Solution](#solution)
  - [Features](#features)
  - [Workflow](#workflow)
  - [Impact of this solution](#impact-of-this-solution)
- [Azure Architechture Diagram](#azure-architechture-diagram)
- [Azure services](#azure-services)
- [Platform Development](#platform-development)
  -  [Power BI Dashboard](#power-bi-dashboard)
- [Benefits](#benefits)
- [Disaster Recovery Plan](#disaster-recovery-plan)
  - [Ensuring Service Recovery](#ensuring-service-recovery)
  - [Ensuring Business Continuity](#ensuring-business-continuity)   
- [Additional Features](#additional-features)
- [Pricing](#pricing) 

# Overview
In partnership with Microsoft Azure, we envision an innovative initiative to drive positive change through the creation of an Advanced Biodiversity Monitoring System for National Parks. This transformative system revolves around the deployment of a state-of-the-art robot, seamlessly integrated with Azure's cutting-edge photo identification AI and image recognition technologies. This solution will empower change by autonomously navigating through national park areas, capturing and analyzing images to meticulously monitor and understand the shifts in biodiversity over time. Together, we aim to harness the power of technology to inspire transformative actions and foster a sustainable, data-driven approach to conservation and environmental stewardship.

### Use case
The following are some key use cases for the *AI-Powered Biodiversity Monitoring System*

**1. Large Scale Organizations and Governments: National Park Management**
Large-scale organizations and government bodies responsible for managing national parks often face challenges in efficiently monitoring and preserving biodiversity. The use of advanced technology can significantly enhance their capabilities. This is the main use case we are considering for the architecture diagram and implementation

**Objective:** Real-time Biodiversity Monitoring and Conservation

**Scenario:**
A national park, spanning vast and diverse landscapes, employs the Advanced Biodiversity Monitoring System. Equipped with robots and Azure-powered infrastructure, the system autonomously collects image data, monitors species distribution, and analyzes environmental conditions.

**Benefits:**
- **Efficient Conservation Management:** Real-time data allows park authorities to proactively address environmental threats, such as invasive species or climate changes.
- **Resource Optimization:** Enables targeted conservation efforts based on specific biodiversity patterns identified through AI analysis.
- **Public Engagement:** The transparent sharing of biodiversity data through the Power BI platform fosters public awareness and support for conservation initiatives.

**2. User Engagement: Environmental Science and Sustainability Promotion**

Promoting user engagement and interest in environmental science and sustainability is crucial for building a community dedicated to conservation efforts.

**Objective:** Inspiring Environmental Awareness and Education

**Scenario:**
The Power BI platform and website are designed for public access, providing an intuitive interface for users to explore the biodiversity data collected from national parks. Interactive visualizations, such as heatmaps and species filters, make it an engaging tool for users of all ages.

**Benefits:**
- **Educational Outreach:** Empowers individuals to explore and understand biodiversity trends, promoting environmental literacy.
- **Inspiration for Conservation:** Visualization of real-world data encourages users to actively participate in conservation activities and support sustainable practices.
- **Community Involvement:** Enables users to contribute observations and engage in discussions about environmental conservation.

**3. Environmental Education for Private and Personal Use**
Individuals interested in environmental education for personal knowledge or academic purposes can leverage the Biodiversity Monitoring System for educational purposes.

**Objective:** Personal Environmental Exploration and Learning

**Scenario:**
Private users, such as students, researchers, or nature enthusiasts, access the Power BI platform to explore biodiversity data. They utilize filters to focus on specific species, locations, or time frames, gaining insights into environmental changes over time.

**Benefits:**
- **Accessible Learning:** Provides a user-friendly platform for personal exploration, enabling self-directed environmental education.
- **Data-Driven Research:** Supports individuals conducting personal research projects or academic studies related to biodiversity and environmental science.
- **Curiosity Cultivation:** Fosters a sense of curiosity and understanding about the natural world, encouraging a lifelong interest in environmental conservation.

**4. Small Areas with Lower Resources: Software Infrastructure for Biodiversity Monitoring**
In areas where deploying physical robots may be challenging due to limited resources, the software infrastructure becomes a valuable resource for understanding biodiversity changes.

**Objective:** Low-Cost Biodiversity Monitoring for Small Areas

**Scenario:**
In smaller areas with lower resources, the focus is on utilizing the Azure cloud-based infrastructure for biodiversity monitoring. The Biodiversity Monitoring System, in this case, relies on image data collected through traditional means (e.g., camera traps) and processes it using Azure services for analysis.

**Benefits:**
- **Cost-Effective Monitoring:** Provides a cost-effective solution for smaller areas without the need for physical robots.
- **Cloud-Based Analysis:** Leverages Azure services for image recognition, allowing for efficient and accurate biodiversity assessments.
- **Data-Driven Conservation:** Even with limited resources, enables evidence-based conservation decisions through the analysis of biodiversity trends over time.

These use cases demonstrate the versatility of the Biodiversity Monitoring System, catering to the diverse needs of large organizations, governments, individual users, and smaller areas with resource constraints. The combination of physical robots, Azure infrastructure, and user-friendly platforms creates a comprehensive solution for environmental monitoring and conservation.

### Stakeholders
Bellow is a breakdown of all potential stakeholders based on our suggested use cases
**Primary Stakeholders:**

1. **Large Scale Organizations and Governments: National Park Management:**
   - National Park Authorities
   - Government Environmental Agencies
   - Conservation Organizations
   - Park Rangers and Field Staff

2. **User Engagement: Environmental Science and Sustainability Promotion:**
   - Environmental Educators
   - Environmental NGOs
   - Educational Institutions
   - Nature Enthusiasts

3. **Environmental Education for Private and Personal Use:**
   - Individual Researchers
   - Citizen Scientists
   - Environmental Educators
   - Nature Photographers

4. **Small Areas with Lower Resources: Software Infrastructure for Biodiversity Monitoring:**
   - Local Environmental Agencies
   - Community Leaders
   - Citizen Scientists
   - Nonprofit Organizations

**Secondary Stakeholders:**

1. **Overall Platform Development and Maintenance:**
   - Software Developers
   - System Architects
   - Data Scientists
   - Project Managers

2. **Azure Services Integration and Maintenance:**
   - Azure Solution Architects
   - Azure Service Administrators
   - Cloud Security Specialists
   - Azure DevOps Teams

3. **Robotics Hardware and Integration:**
   - Roboticists
   - Hardware Engineers
   - Integration Specialists

4. **Species Classification and AI Model Development:**
   - Data Scientists
   - Machine Learning Engineers
   - AI Researchers
   - Biologists and Ecologists

**Tertiary Stakeholders:**

1. **Public and Community Engagement:**
   - Social Media Managers
   - Public Relations Teams
   - Community Outreach Coordinators

2. **Regulatory Compliance and Ethics:**
   - Legal Advisors
   - Regulatory Compliance Officers
   - Data Privacy Experts
   - Ethics Review Board Members

3. **Overall Platform Development and Maintenance:**
   - User Experience (UX) Designers
   - Quality Assurance (QA) Teams
   - DevOps Engineers

4. **Large Scale Organizations and Governments: National Park Management:**
   - Environmental Scientists and Researchers
   - Local Communities
   - Tourist Boards

5. **Public and Community Engagement:**
   - Environmental Activists
   - Community Leaders
   - Local Government Representatives
   - Advocacy Groups

## Solution
general info 

### Features 
1. **Automated Image Recognition:**
   - Utilize Azure Cognitive Services, particularly Azure Computer Vision, to enable the robot to identify and categorize various plant and animal species from images captured during its walks.

2. **Environmental Monitoring:**
   - Integrate Azure IoT Hub for real-time data collection from on-board sensors that monitor climate conditions, enabling the system to assess the environmental health of the area.

3. **Invasive Species Detection:**
   - Implement Azure Machine Learning to train the system to recognize invasive species, enabling early detection and timely intervention to preserve the ecosystem.

4. **Waste and Pollution Tracking:**
   - Leverage Azure Custom Vision to train the robot to identify instances of litter or pollution, enabling the system to notify park authorities for necessary cleanup.

5. **Safety and Reduced Human Disturbance:**
   - Deploy Microsoft's autonomous robot technology, ensuring it navigates through sensitive areas without causing disturbances, reducing the need for manual monitoring by humans.
 
### Workflow
info 
### Impact of this solution
The development of an Advanced Biodiversity Monitoring System for National Parks, powered by Microsoft Azure, is of paramount importance for several compelling reasons:

1. **Conservation Impact:**
   - Enables real-time monitoring of biodiversity, providing crucial data for informed conservation strategies and fostering the preservation of delicate ecosystems within national parks.

2. **Early Detection of Threats:**
   - Facilitates the early identification of potential threats such as invasive species and pollution, enabling rapid intervention and mitigating risks to the park's ecosystem.

3. **Scientific Research Opportunities:**
   - Creates a valuable repository of high-quality data, opening new frontiers for scientific research on biodiversity patterns, climate change impacts, and ecosystem dynamics.

4. **Efficiency and Accuracy:**
   - Utilizes Azure's advanced AI and image recognition technologies to ensure precise species identification, surpassing human capabilities and enhancing the accuracy of biodiversity monitoring.

5. **Minimized Human Disturbance:**
   - Employs an autonomous robot to navigate through national park areas, minimizing human interference and disturbance to wildlife, thereby fostering a more sustainable approach to environmental monitoring.

6. **Community Engagement and Education:**
   - Engages the community through Azure-powered platforms, fostering a sense of environmental responsibility and educating the public on the importance of biodiversity conservation.

7. **Adaptation to Climate Change:**
   - Provides critical data for understanding how biodiversity adapts to climate change, offering insights that can inform adaptive management strategies to safeguard vulnerable species.

8. **Enhanced Resource Allocation:**
   - Enables efficient allocation of conservation resources by pinpointing specific areas of concern, optimizing efforts, and ensuring that interventions are targeted where they are needed the most.

9. **Data-Driven Decision Making:**
   - Empowers park authorities and conservationists with actionable insights, facilitating data-driven decision-making processes for more effective and impactful biodiversity management.

10. **Contributions to Global Environmental Goals:**
    - Aligns with global initiatives for biodiversity conservation, contributing to broader environmental goals and commitments to protect and sustain the planet's diverse ecosystems.

In essence, the implementation of this Biodiversity Monitoring System not only leverages cutting-edge technology but also represents a pivotal step towards fostering positive change, sustainable conservation practices, and the empowerment of communities to actively participate in the preservation of our natural heritage.

## Azure Architechture Diagram
Image and doc

## Azure services
Content for Subsection 2.2...

## Platform Development
platform description 

### Power BI Dashboard
specific things on the dashboard

## Benefits
Below is a summary of the benefits of implementing the AI-Powered Biodiversity Monitoring System
1. **Data-Driven Conservation Strategies:**
   - The system enables data collection on a large scale, facilitating the development of informed conservation strategies based on historical and real-time data.

2. **Real-Time Alerts and Notifications:**
   - Azure services provide the capability to set up real-time alerts, ensuring immediate responses to emerging issues such as invasive species, pollution, or significant biodiversity changes.

3. **Enhanced Collaboration and Community Engagement:**
   - Utilizing Azure DevOps for community engagement promotes collaboration between park authorities, researchers, and the public, fostering a collective effort in environmental preservation.

4. **Reduced Carbon Footprint:**
   - By employing autonomous robots for monitoring instead of traditional methods involving human intervention, the system contributes to a reduction in the carbon footprint associated with manual surveillance.

5. **Remote Monitoring and Management:**
   - Azure's cloud-based services allow for remote monitoring and management of the entire system, reducing the need for on-site personnel and ensuring efficient operation from anywhere.

6. **Predictive Maintenance:**
   - Azure IoT services enable predictive maintenance for the robot, ensuring optimal performance by identifying potential issues before they become critical, reducing downtime and maintenance costs.

7. **Regulatory Compliance:**
   - The system can aid in meeting regulatory requirements for environmental monitoring and reporting, ensuring that the national parks adhere to conservation standards.

8. **Scalable Resource Allocation:**
   - Azure's scalability allows for the easy addition of robots or sensors as needed, ensuring optimal resource allocation based on the size and characteristics of different national park areas.

9. **Improved Research Opportunities:**
   - The system provides a rich source of data for researchers and scientists, opening up opportunities for biodiversity studies, climate change research, and ecosystem analysis.

10. **Enhanced Public Awareness:**
    - The community engagement platform can serve as an educational tool, raising public awareness about the importance of biodiversity conservation and promoting a sense of responsibility among park visitors.

11. **Adaptability to Park-Specific Needs:**
    - Azure's flexibility enables the customization of the solution to cater to the unique requirements of different national parks, ensuring adaptability to diverse ecosystems.

12. **Preservation of Human Safety:**
    - By deploying robots in potentially hazardous or remote areas, the system minimizes the risk to human safety associated with manual monitoring in challenging terrains.

These benefits collectively showcase the comprehensive advantages that the proposed Biodiversity Monitoring System can bring to national parks, aligning with Microsoft Azure's capabilities for efficient, scalable, and secure cloud-based solutions.

## Disaster Recovery Plan
### Ensuring Service Recovery
**1. Risk Assessment:**
   - Conduct regular risk assessments to identify potential disasters, and their impact on business operations, and prioritize recovery efforts.

**2. Data Backup:**
   - Implement regular data backups using Azure Backup Services to ensure critical business data is protected and can be restored in case of data loss.

**3. Azure Site Recovery (ASR):**
   - Utilize Azure Site Recovery for replicating virtual machines and ensuring a quick recovery in case of a site-wide disaster, enabling seamless failover to a secondary Azure region.

**4. Redundancy and Load Balancing:**
   - Leverage Azure Traffic Manager and Azure Load Balancer to distribute application traffic across multiple regions, ensuring redundancy and high availability.

**5. Virtual Machine Snapshots:**
   - Regularly capture snapshots of virtual machines using Azure Virtual Machine backups, allowing for quick recovery to a specific point in time.

**6. Azure Blob Storage for Data Resilience:**
   - Use Azure Blob Storage for durable and highly available cloud storage, ensuring the availability of critical data even in the event of local infrastructure failures.

### Ensuring Business Continuity:

**1. Azure Site Recovery (ASR):**
   - ASR ensures continuous replication of workloads to a secondary Azure region, enabling failover in case of a primary data center failure, providing a geographically dispersed disaster recovery solution.

**2. Azure Backup:**
   - Azure Backup automates the backup of on-premises and cloud data, ensuring that critical information is regularly saved and can be restored efficiently.

**3. Azure Traffic Manager:**
   - By using Traffic Manager, businesses can distribute user traffic across multiple Azure regions, ensuring high availability and minimizing downtime during disasters.

**4. Azure Load Balancer:**
   - Load Balancer distributes incoming network traffic across multiple servers, ensuring that applications remain available and responsive, even in the face of server failures.

**5. Azure Virtual Machine Backups:**
   - Azure VM backups allow for the creation of recovery points, providing flexibility in restoring virtual machines to a specific state in case of data corruption or loss.

**6. Geo-Redundant Storage:**
   - Geo-Redundant Storage in Azure replicates data to a secondary region, providing an additional layer of protection against data loss and ensuring data availability.

**7. Azure Security and Compliance:**
   - Azure's robust security features, including encryption, access controls, and compliance certifications, contribute to a secure and resilient environment for business operations during and after a disaster.

**8. Azure Resource Manager (ARM) Templates:**
   - Use ARM templates to define and deploy Azure resources in a consistent and repeatable manner, aiding in the rapid rebuilding of the infrastructure in case of a disaster.

**9. Azure Monitor and Azure Security Center:**
   - Azure Monitor provides real-time insights into the performance and health of applications, while Azure Security Center helps in identifying and mitigating security threats, ensuring a secure and monitored environment.

**10. Regular Testing and Drills:**
    - Conduct regular disaster recovery drills and testing to validate the effectiveness of the plan, ensuring that personnel are familiar with recovery procedures and can respond promptly during an actual disaster.

This disaster recovery plan, coupled with the use of Azure services, provides a comprehensive approach to ensuring business continuity, data resilience, and a rapid response to unforeseen events. Regular updates and testing are crucial to maintaining the effectiveness of the plan over time.

## Additional Features
1. **Community Engagement:**
   - Integrate Azure DevOps to create a community engagement platform where park visitors can contribute observations and data, fostering a sense of environmental responsibility.

2. **Historical Data Analysis:**
   - Use Azure Time Series Insights to store and analyze historical data, allowing for long-term trend analysis and better-informed conservation strategies.

3. **AI-driven Alerts:**
   - Implement Azure Logic Apps to trigger automated alerts for park rangers based on identified changes, streamlining response times to potential issues.


## Pricing



