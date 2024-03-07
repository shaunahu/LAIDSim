# An LLM-enhanced Agent-based Simulation Tool for Information Propagation
## Introduction
This is a LLM-enhanced Agent-based Influence Diffusion Simulation tool (LAIDSim) to simulate the information propagation phenomenon in social networks. It enables users to manipulate various parameters, design different application settings, and visualize the diffusion process. It also plots the real-time analysis results in terms of influence coverage and alteration degree.

## Installation
This tool is developed based on [Melodie](https://github.com/ABM4ALL/Melodie) and [MelodieStudio](https://github.com/ABM4ALL/MelodieStudio). Please ensure these two packages have been installed.

## Initialization
To start with, set parameters in 'data/input/SimulatorScenarios.xlsx'. Below is a breif introduction of these parameters:
 - id: scenario id
 - run_num: numbers of time to run a simulation
 - period_num: numbers of timesteps in one round simulation
 - agent_num: numbers of user agents in a social network
 - network_type: random network type, align with [Networkx graph generators](https://networkx.org/documentation/stable/reference/generators.html).
 - network_param_directed: is a directed graph or not.
 - network_param_p: erdos_renyi graph parameter, this should also align with Networkx graph generators.
 - seed_size: numbers of initial influencers.
 - influence_message: the original message sent by seeds.

## Run
Go to the path of current project, in console, run `python -m MelodieStudio`. This should connect to the MelodieStudio server. Once it started, run 'run_simulator.py'.

