
# Lab02B - Linux Ubuntu VM CPU and Memory Analysis Report

**Student Name:** Michael Belette 
**Student ID:** [Your Student ID]  
**Course Section:** SPR 100 
**Completion Date:** 2026/02/06  
**Lab Duration:** 2.5 hrs

---

## Part 1: Ubuntu VM Setup and Configuration

### 1.1 VM Configuration Summary
- **Hypervisor:** VMware Workstation Pro
- **Version:** 17 
- **CPU Cores:** 2
- **Memory:** 4 GB (Allocated) / 3.8 GiB (Detected)
- **Storage:** 20 GB NVMe
- **Network:** NAT

### 1.2 VM Installation and Startup Process
- **Ubuntu ISO Source:** School Network Drive (\\mydrive\courses\SPR100\)
- **Installation Method:** Imported from a pre-configured .ova appliance
- **Startup Time:** 45 seconds
- **User Account Created:** ubuntu
- **Initial VM State:** Successful boot to CLI; blind password entry caused initial login confusion

---

## Part 2: Linux System Analysis

### 2.1 CPU Analysis Results

#### System Information Commands
- **Processor Information:** Intel(R) Core(TM) Ultra 7 155H with 30 MiB L3 Cache
- **Architecture:** x86_64
- **Number of Cores:** 2
- **CPU Model Name:** Intel(R) Core(TM) Ultra 7 155H
- **CPU Frequency:** 1400.000 MHz

#### htop CPU Analysis
- **Current CPU Usage:** 0.0% – 3.1%
- **Number of CPU Cores Visible:** 2
- **CPU Utilization Pattern:** Consistent idle state at 0% with momentary spikes to 3.1% during command execution
- **Process CPU Usage:** top, grep, and kworker

#### Linux Command Outputs
    # Processor Information Command Output:
    Architecture:            x86_64
CPU(s):                  2
Vendor ID:               GenuineIntel
Model name:              Intel(R) Core(TM) Ultra 7 155H
Virtualization features: VMware (full)
L3 cache:                30 MiB

    # CPU Performance Output:
    %Cpu(s): 0.0 us, 3.1 sy, 0.0 ni, 96.9 id, 0.0 wa, 0.0 hi, 0.0 si, 0.0 st

### 2.2 Memory Analysis Results

#### System Information Memory Details
- **Total Physical Memory:** 3.8 GiB
- **Available Physical Memory:** 3.3 GiB
- **Memory Usage Pattern:** Linear and stable; used memory stayed at 297 MiB
- **Buffer and Cache Information:** 367 MiB used for system optimization

#### Linux Memory Commands Output
    # Memory Information:
    total        used        free      shared  buff/cache   available
Mem:           3.8Gi       297Mi       3.1Gi       1.0Mi       367Mi       3.3Gi

    # Memory Performance:
    MemTotal: 3921844 kB | MemFree: 3254124 kB | MemAvailable: 3456712 kB

### 2.3 System Performance Monitoring Results

#### Performance Monitoring Script
- **Monitoring Duration:** [2 minutes]
- **Sample Interval:** [5 seconds]
- **CPU Usage Range:** 0.0% – 3.1%
- **Memory Usage Range:** 7.6% (Consistent at 297 MiB)
- **Performance Patterns Observed:** System showed almost zero CPU stress while idle, with a tiny 3.1% spike only when the monitoring script was actively pulling data.

#### htop Resource Monitor Observations
- **Peak CPU Usage:** 3.1%
- **Peak Memory Usage:** 297 MiB (or 7.6%)
- **Resource Usage During Activities:** The system maintained a stable idle state with nearly 0% CPU usage. A minor spike to 3.1% 
was observed only when the performance monitoring script was actively executing commands. Memory usage remained completely flat throughout all activities.

---

## Part 3: Security and Virtualization Analysis

### 3.1 Linux Security Features Status
- **AppArmor Status:** Enabled
- **UFW Firewall Status:** Active
- **UFW Rules Summary:** Default deny (incoming), allow (outgoing); no custom rules currently defined
- **System Updates Status:** Security updates verified as current during the last apt check at boot

### 3.2 VM Isolation Test Results

#### File System Isolation
- **Test File Created:** lab_test.txt in /home/ubuntu/
- **Host System Check:** no
- **Isolation Effectiveness:** Highly effective; the guest OS is encapsulated within a virtual disk file (.vmdk), 
ensuring that files created inside Linux are inaccessible to the host Windows environment.

#### Process Isolation
- **VM Processes Observed:** systemd, kthreadd, rcu_gp, rcu_par_gp, slub_flush_wq
- **Host Processes Visible:** no
- **Isolation Observations:** Only Linux-specific kernel and user processes are visible in the VM;
 this prevents potentially compromised guest software from interacting with or monitoring host system activities.

### 3.3 Performance Observation Results

#### CPU Performance Comparison
- **VM CPU Usage:** 0.0% – 3.1%
- **Host CPU Usage:** Approximately 5% – 8%
- **Performance Differences:** The host usage is slightly higher because
 it must run the VMware hypervisor application and handle background Windows tasks in addition to the VM load.
#### Memory Performance Test
- **Applications Opened:** Terminal, top, free, and the monitoring script
- **Initial Memory Usage:** 297 MiB
- **Final Memory Usage:** 297 MiB
- **Memory Behavior Observations:** Usage remained perfectly flat and stable; since no heavy graphical applications were launched,
 the CLI environment maintained a very low and consistent memory footprint.

---

## Analysis and Conclusions

### Key Findings
1. **CPU Performance:** The system remained highly stable with an idle
 usage of 0.0%, showing that the Intel Core Ultra 7 155H handles virtualized loads with minimal stress.
2. **Memory Performance:** Memory usage was remarkably consistent at 297 MiB, utilizing only about 7.6% of the available 3.8 GiB.
3. **Virtualization Overhead:** The VM reports 3.8 GiB of RAM even though 4 GB was allocated; this small difference represents the memory "overhead" taken 
by the hypervisor to manage the virtual hardware.
4. **Security Features:** The VM is secured by default with AppArmor profiles and an active UFW firewall, providing a robust "deny-by-default" security posture.

### Technical Insights
- **Linux System Understanding:** I learned that Linux distinguishes between "Free" and "Available" memory, 
where available memory includes reclaimable cache that the system can use if needed.
- **Virtualization Concepts:** I learned that hypervisors provide hardware 
isolation, meaning the guest OS (Ubuntu) cannot see or interact with the host (Windows) processes or files.
- **Performance Monitoring:** I learned how to use terminal-based tools like top and free within a bash loop to capture real-time performance snapshots.

### Challenges and Solutions
- **Challenges Faced:** Entering the password at the login prompt was confusing because no characters or dots appeared on the screen.
- **Solutions Applied:** I learned this is a standard Linux security feature and completed the login by typing the password "blind" and pressing Enter.
- **Lessons Learned:** I would check the course documentation first to verify default credentials and terminal behavior before assuming a hardware input error.

---

**Report Completion Time:** 2.5 hrs  
**Confidence Level:** 6.5 
**Questions for Instructor:** How does the hypervisor decide which physical CPU features (like specific AVX instructions) to expose to the virtual machine?
