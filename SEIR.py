import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 🧮 SEIR Model
def seir_model(S0, E0, I0, R0, beta, sigma, gamma, days):
    S, E, I, R = [S0], [E0], [I0], [R0]
    N = S0 + E0 + I0 + R0

    for _ in range(days):
        next_S = S[-1] - beta * S[-1] * I[-1] / N
        next_E = E[-1] + beta * S[-1] * I[-1] / N - sigma * E[-1]
        next_I = I[-1] + sigma * E[-1] - gamma * I[-1]
        next_R = R[-1] + gamma * I[-1]

        S.append(next_S)
        E.append(next_E)
        I.append(next_I)
        R.append(next_R)

    return np.array(S), np.array(E), np.array(I), np.array(R)

# 📌 UI
st.title("จำลองการระบาดของโรคด้วย SEIR Model 🧫")

st.sidebar.header("Parameter Input Panel")
population = st.sidebar.number_input("ประชากรทั้งหมด (N)", value=1000)
initial_exposed = st.sidebar.number_input("จำนวนผู้ที่ได้รับเชื้อแต่ยังไม่แสดงอาการ (E0)", value=1)
initial_infected = st.sidebar.number_input("จำนวนผู้ติดเชื้อเริ่มต้น (I0)", value=1)
initial_recovered = st.sidebar.number_input("จำนวนผู้ฟื้นตัวเริ่มต้น (R0)", value=0)

beta = st.sidebar.slider("อัตราการติดเชื้อ (β)", 0.0, 1.0, 0.3)
sigma = st.sidebar.slider("อัตราการเข้าสู่การติดเชื้อ (σ)", 0.0, 1.0, 0.1)
gamma = st.sidebar.slider("อัตราการฟื้นตัว (γ)", 0.0, 1.0, 0.1)
days = st.sidebar.slider("จำนวนวันในการจำลอง", 1, 365, 100)

# 🔄 เริ่มจำลอง
if st.button("เริ่มการจำลอง"):
    S0 = population - initial_exposed - initial_infected - initial_recovered
    S, E, I, R = seir_model(S0, initial_exposed, initial_infected, initial_recovered, beta, sigma, gamma, days)

    # 📈 แสดงผล
    st.subheader("ผลการจำลองการระบาด")
    fig, ax = plt.subplots()
    ax.plot(S, label="S")
    ax.plot(E, label="E")
    ax.plot(I, label="I")
    ax.plot(R, label="R")
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.legend()
    st.pyplot(fig)# Auto detect text files and perform LF normalization
* text=auto
