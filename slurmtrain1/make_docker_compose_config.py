#!/usr/bin/env python3

fout = open("docker-compose.yml", "wt")
compute_reg = 1

fout.write("""version: "3.8"
services:
  headnode:
    image: nsimakov/slurm_head_node:3
    hostname: headnode
    shm_size: 64M
    command: ["sshd", "munged", "mysqld", "/opt/cluster/vctools/add_system_users.sh", "-loop"]
    # "/opt/cluster/vctools/start_head_node.sh" is intentionally removed here
    # run_vc.sh will start slurm services in right order and will track time
    networks:
      network1:
        ipv4_address: 172.32.0.11
    volumes:
      - './results:/root/results'
      - './etc:/etc/slurm'
      - './vctools:/opt/cluster/vctools'
      - './job_traces:/opt/cluster/job_traces'
      - './_log:/var/log/slurm'
      - './_home:/home'
      - './../../slurm_sim_tools:/opt/cluster/slurm_sim_tools'
    cpuset: '0-3'
""")


def get_compute_node_volumes(nodename):
    return f"""volumes:
      - './results:/root/results'
      - './etc:/etc/slurm'
      - './vctools:/opt/cluster/vctools'
      - './job_traces:/opt/cluster/job_traces'
      - './_compute_nodes_log/{nodename}:/var/log/slurm'
      - './_home:/home'"""\

for i in range(1,compute_reg+1):
    hostname = f"  compute{i:d}"
    ip = i+100
    fout.write(f"""{hostname}:
    image: nsimakov/slurm_compute_node:3
    hostname: {hostname}
    command: ["sshd", "munged", "/opt/cluster/vctools/start_compute_node.sh", "-loop"]
    networks:
      network1:
        ipv4_address: 172.32.2.{ip}
    {get_compute_node_volumes(hostname)}
    cpuset: '4-7'
""")

fout.write("""networks:
  network1:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: "172.32.0.0/21"
""")
