import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Pretext Dashboard",
    layout="wide"
)


@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/dataset_pretext.csv"
    )

    if "Unnamed: 0" in df.columns:
        df = df.drop(
            columns=["Unnamed: 0"]
        )

    return df


df = load_data()

st.title(
    "Career Analytics Dashboard"
)

st.markdown(
    "Analisis Career Confusion Dataset"
)

st.sidebar.header("Filter Data")

selected_roles = st.sidebar.multiselect(
    "Target Role",
    sorted(
        df["target_role"].unique()
    )
)

selected_level = st.sidebar.multiselect(
    "Current Level",
    sorted(
        df["current_level"].unique()
    )
)

selected_problem = st.sidebar.multiselect(
    "Problem Category",
    sorted(
        df["problem_category"].unique()
    )
)

filtered_df = df.copy()

if selected_roles:
    filtered_df = filtered_df[
        filtered_df["target_role"]
        .isin(selected_roles)
    ]

if selected_level:
    filtered_df = filtered_df[
        filtered_df["current_level"]
        .isin(selected_level)
    ]

if selected_problem:
    filtered_df = filtered_df[
        filtered_df["problem_category"]
        .isin(selected_problem)
    ]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Users",
    len(filtered_df)
)

col2.metric(
    "Unique Roles",
    filtered_df["target_role"]
    .nunique()
)

col3.metric(
    "Problem Categories",
    filtered_df["problem_category"]
    .nunique()
)

col4.metric(
    "Blocker Types",
    filtered_df["blocker_type"]
    .nunique()
)

st.divider()

st.subheader(
    "Top Career Goals"
)

role_count = (
    filtered_df["target_role"]
    .value_counts()
    .head(15)
    .reset_index()
)

role_count.columns = [
    "target_role",
    "total_users"
]

fig_role = px.bar(
    role_count,
    x="total_users",
    y="target_role",
    orientation="h",
    labels={
        "total_users": "Jumlah",
        "target_role": "Role"
    }
)

st.plotly_chart(
    fig_role,
    use_container_width=True
)

st.divider()

left, right = st.columns(2)

with left:

    st.subheader(
        "Problem Category Distribution"
    )

    problem_count = (
        filtered_df["problem_category"]
        .value_counts()
    )

    fig_problem = px.pie(
        values=problem_count.values,
        names=problem_count.index
    )

    st.plotly_chart(
        fig_problem,
        use_container_width=True
    )

with right:

    st.subheader(
        "Current Level Distribution"
    )

    level_count = (
    filtered_df["current_level"]
    .value_counts()
    .reset_index()
)

    level_count.columns = [
        "current_level",
        "total_users"
    ]

    fig_level = px.bar(
        level_count,
        x="current_level",
        y="total_users",
        labels={
            "current_level": "Current Level",
            "total_users": "Jumlah User"
        }
    )

    st.plotly_chart(
        fig_level,
        use_container_width=True
    )

st.divider()

st.subheader(
    "Level vs Problem Category"
)

cross = pd.crosstab(
    filtered_df["current_level"],
    filtered_df["problem_category"]
)

fig_cross = px.bar(
    cross.reset_index().melt(
        id_vars="current_level"
    ),
    x="current_level",
    y="value",
    color="problem_category",
    barmode="group"
)

st.plotly_chart(
    fig_cross,
    use_container_width=True
)

st.divider()

st.subheader(
    "Raw Dataset"
)

st.dataframe(
    filtered_df,
    use_container_width=True
)