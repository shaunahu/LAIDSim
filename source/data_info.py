import sqlalchemy

from Melodie import DataFrameInfo

simulator_scenarios = DataFrameInfo(
    df_name='simulator_scenarios',
    file_name='SimulatorScenarios.xlsx',
    columns={
        "id": sqlalchemy.Integer(),
        "run_num": sqlalchemy.Integer(),
        "period_num": sqlalchemy.Integer(),
        "agent_num": sqlalchemy.Integer(),
        "network_type": sqlalchemy.String(),
        "network_param_p": sqlalchemy.Float(),
        "network_param_directed": sqlalchemy.String(),
        "item_num": sqlalchemy.Integer(),
        "initial_infected_percentage": sqlalchemy.Float(),
        "infection_prob": sqlalchemy.Float()
    },
)

id_preference_state = DataFrameInfo(
    df_name="ID_PreferenceState",
    file_name="ID_PreferenceState.xlsx",
    columns={
        "id": sqlalchemy.Integer(),
        "name": sqlalchemy.String()
    },
)

agent_params = DataFrameInfo(
    df_name="Parameter_AgentParams",
    columns={
        "id_scenario": sqlalchemy.Integer(),
        "id": sqlalchemy.Integer(),
        "preference_state": sqlalchemy.Integer(),
    },
)
