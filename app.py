import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Configuration & Styling ---
st.set_page_config(
    page_title="IPL Economics & Personal Finance",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .reportview-container {
        background: #0f1115;
    }
    .metric-value {
        font-size: 2.5rem !important;
        font-weight: 800;
        color: #00E676;
    }
    .metric-label {
        font-size: 1.1rem;
        color: #B0BEC5;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .learning-card {
        background: #1E2329;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00E676;
        margin-bottom: 20px;
    }
    .learning-title {
        color: #FFFFFF;
        font-size: 1.4rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .learning-text {
        color: #CFD8DC;
        font-size: 1.05rem;
        line-height: 1.6;
    }
    .stRadio > div {
        background: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a Module:", [
    "1. The IPL Ecosystem & AI",
    "2. Ad-Sense & Sponsorship Trends",
    "3. Science of Franchise Valuations",
    "4. Impact on Indian Economy",
    "5. Financial Learnings"
])

st.sidebar.divider()
st.sidebar.caption("Data points presented are estimates based on public records for educational purposes.")

# ==========================================
# PAGE 1: The Ecosystem & AI
# ==========================================
if page == "1. The IPL Ecosystem & AI":
    st.title("📈 The Business of IPL & The Role of AI")
    st.markdown("Discover the multi-billion dollar ecosystem and how Artificial Intelligence is revolutionizing its finance.")

    st.divider()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### Estimated 2026 Ecosystem Valuation")
        
        m1, m2 = st.columns(2)
        with m1:
            st.markdown('<div class="metric-label">Total Brand Value</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-value">$11.2 Billion</div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="metric-label">Media Rights (5 Years)</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-value">₹48,390 Cr</div>', unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("### 🤖 How AI & Finance Play a Role")
        st.info("**1. Dynamic Ad Pricing:** Just like Uber surge pricing, AI algorithms now predict 'High-Leverage Moments' (death overs, Kohli batting) to dynamically increase Connected TV ad rates in real-time.")
        st.info("**2. Player Auction Quants:** Teams use advanced machine learning to run Monte Carlo simulations on player performance vs. cost, ensuring maximum ROI on their salary caps.")
        st.info("**3. Sponsor ROI Tracking:** AI computer vision scans the broadcast to track logo visibility on jerseys and boundaries, calculating the exact second-by-second ROI for sponsors.")

    with col2:
        # Revenue Stream Breakdown Data
        revenue_data = {
            'Category': ['Media Rights (TV & Digital)', 'Central Sponsorships', 'Franchise Sponsorships', 'Ticket Sales', 'Merchandising'],
            'Percentage': [65, 15, 10, 7, 3],
            'Pool': ['Central', 'Central', 'Local', 'Local', 'Local']
        }
        df_rev = pd.DataFrame(revenue_data)
        
        fig = px.pie(
            df_rev, 
            values='Percentage', 
            names='Category', 
            hole=0.4,
            color_discrete_sequence=px.colors.sequential.Tealgrn,
            title="Revenue Pool Breakdown"
        )
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='white', margin=dict(t=40, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)

# ==========================================
# PAGE 2: Ad-Sense & Sponsorship Trends
# ==========================================
elif page == "2. Ad-Sense & Sponsorship Trends":
    st.title("📺 Ad-Sense & Sponsorship Trends (YoY)")
    st.markdown("How brand investments have compounded over the years, shifting from Linear TV to Digital.")

    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Title Sponsorship Growth")
        # Dummy data showing exponential growth
        years = [2008, 2013, 2016, 2018, 2022, 2024, 2026]
        sponsors = ['DLF', 'Pepsi', 'Vivo', 'Vivo', 'Tata', 'Tata', 'Tata (Est)']
        values = [40, 79, 100, 440, 600, 600, 750] # Crores per year roughly
        
        df_sponsors = pd.DataFrame({'Year': years, 'Sponsor': sponsors, 'Value (Cr/Year)': values})
        
        fig_sponsors = px.line(df_sponsors, x='Year', y='Value (Cr/Year)', text='Sponsor', markers=True)
        fig_sponsors.update_traces(textposition="bottom right", line_color='#00E676')
        fig_sponsors.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig_sponsors, use_container_width=True)

    with col2:
        st.markdown("### 10-Second Ad Rate Evolution")
        years_ad = [2008, 2014, 2018, 2022, 2026]
        tv_rates = [2.5, 4.5, 10.0, 14.0, 18.0] # Lakhs
        ctv_rates = [0, 0.5, 3.0, 12.0, 21.5] # Lakhs (CTV explosion)
        
        df_ads = pd.DataFrame({
            'Year': years_ad * 2,
            'Rate (Lakhs)': tv_rates + ctv_rates,
            'Platform': ['Linear TV']*5 + ['Digital / CTV']*5
        })
        
        fig_ads = px.bar(df_ads, x='Year', y='Rate (Lakhs)', color='Platform', barmode='group', color_discrete_sequence=['#29B6F6', '#FFA000'])
        fig_ads.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig_ads, use_container_width=True)
        
    st.markdown("### The Digital Flippening")
    st.write("Notice how Digital/CTV ad rates have surpassed traditional TV by 2026. Advertisers are willing to pay a premium (₹21.5L vs ₹18L) because digital platforms allow for targeted ads and interactive 'shoppable' formats, increasing conversion rates compared to passive TV viewing.")

# ==========================================
# PAGE 3: Science of Franchise Valuations
# ==========================================
elif page == "3. Science of Franchise Valuations":
    st.title("💰 The Science of Franchise Valuations")
    st.markdown("How do teams that bought in for ₹400 Cr in 2008 reach $1B+ (₹8,000+ Cr) valuations today?")

    st.divider()
    
    st.markdown("### How is it calculated?")
    st.write("Sports franchises aren't valued like traditional software companies. They are valued primarily on **Revenue Multiples** and **Brand Equity Scarcity**.")
    
    c1, c2, c3 = st.columns(3)
    c1.info("**1. The Revenue Multiple:** Because sports leagues operate like cartels with guaranteed revenues (media rights), teams trade at massive multiples of their annual revenue—typically 8x to 12x.")
    c2.info("**2. Scarcity Premium:** There are only 10 IPL teams. Billionaires want to own them for prestige. When supply is absolutely fixed and demand is infinite, the valuation skyrockets.")
    c3.info("**3. Brand Equity:** Teams like CSK and MI command a higher multiple because their merchandise sales and local sponsor pull are significantly higher than newer teams.")
    
    st.divider()
    
    st.markdown("### 🧮 Interactive Valuation Calculator")
    st.write("Calculate the valuation of a hypothetical franchise based on standard financial modeling.")
    
    col1, col2 = st.columns(2)
    with col1:
        central_revenue = st.slider("Central Revenue Pool Share (Media Rights) - ₹ Cr", 200, 600, 450)
        local_revenue = st.slider("Local Revenue (Tickets, Sponsors, Merch) - ₹ Cr", 50, 300, 150)
        multiple = st.slider("Revenue Multiple (Based on Brand Equity)", 6.0, 14.0, 9.5)
        
    with col2:
        total_revenue = central_revenue + local_revenue
        valuation = total_revenue * multiple
        
        st.markdown('<div class="metric-label" style="text-align: center;">Total Annual Revenue</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="metric-value" style="text-align: center; color: #29B6F6;">₹{total_revenue} Cr</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown('<div class="metric-label" style="text-align: center;">Estimated Franchise Valuation</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="metric-value" style="text-align: center;">₹{valuation:,.0f} Cr</div>', unsafe_allow_html=True)
        if valuation >= 8300:
            st.markdown('<div style="text-align: center; color: gold; font-weight: bold;">🏆 Unicorn Status ($1B+)</div>', unsafe_allow_html=True)

# ==========================================
# PAGE 4: Impact on Indian Economy
# ==========================================
elif page == "4. Impact on Indian Economy":
    st.title("🏗️ Driving the Indian Economy")
    st.markdown("The IPL acts as a massive, recurring economic stimulus package.")

    st.divider()

    eco_col1, eco_col2, eco_col3 = st.columns(3)

    with eco_col1:
        st.markdown("### 🏨 Hospitality Boom")
        st.write("Host cities see massive surges in hotel occupancies (up 40-50% on match days). Airline travel spikes as fans move across the country. Local restaurants, pubs, and food delivery apps report a 20-30% surge in orders during match hours.")

    with eco_col2:
        st.markdown("### 💼 Job Creation")
        st.write("Direct and indirect employment for thousands. This includes event management staff, private security, logistics, transportation, content creators, broadcast technicians, and stadium personnel working intensely over a 2-month window.")

    with eco_col3:
        st.markdown("### 🏦 Tax Revenue")
        st.write("The ecosystem generates massive GST (from ticket sales to sponsorship invoices) and income tax for the government. Players, foreign staff, and broadcasting agencies all contribute heavily to the exchequer.")

    st.divider()
    
    st.markdown("### 🏙️ Tier-2 City Structural Changes")
    st.write("As the IPL expands, it drives structural changes outside major metros (Mumbai, Delhi, Bangalore).")
    st.write("- **Infrastructure Development:** New stadiums in cities like Lucknow, Ahmedabad, and Guwahati force the development of surrounding metro lines, roads, and luxury hotels.")
    st.write("- **Grassroots Academies:** The influx of local franchise money has led to world-class coaching centers being built in smaller towns, democratizing access to elite sports training.")

# ==========================================
# PAGE 5: Financial Learnings
# ==========================================
elif page == "5. Financial Learnings":
    st.title("🧠 Financial Learnings for the Common Man")
    st.markdown("Look beyond the cricket. The business models powering the IPL offer profound lessons for personal wealth management.")

    st.divider()

    st.markdown("""
    <div class="learning-card">
        <div class="learning-title">1. Media Rights = The Power of Passive/Scalable Income</div>
        <div class="learning-text">
            <strong>The Business:</strong> The BCCI doesn't play the matches, yet they earn ₹48,000+ Crores just by licensing the rights to broadcast it. They build the product once and sell the distribution rights.<br><br>
            <strong>Your Lesson:</strong> Trading time for money (a salary) has a ceiling. Wealth is built by creating or acquiring assets that generate passive or scalable income—like building software, writing a book, investing in dividend stocks, or licensing your expertise.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="learning-card">
        <div class="learning-title">2. Franchise Valuation = Long-Term Asset Appreciation</div>
        <div class="learning-text">
            <strong>The Business:</strong> Teams bought for ₹400 Crores in 2008 are now valued at ₹8,000+ Crores. The real money wasn't made in year-to-year operational profits, but in holding a scarce asset as it appreciated over 15 years.<br><br>
            <strong>Your Lesson:</strong> Stop chasing quick trading profits. Real wealth is made by buying high-quality, scarce assets (index funds, real estate, solid businesses) and holding them for decades to let compounding and market growth do the heavy lifting.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="learning-card">
        <div class="learning-title">3. Diverse Revenue Streams = Financial Security</div>
        <div class="learning-text">
            <strong>The Business:</strong> Franchises don't rely solely on ticket sales. They get a share of the central broadcast pool, title sponsors, local sponsors, and merchandise. If rain washes out a match, they don't go bankrupt.<br><br>
            <strong>Your Lesson:</strong> A single source of income (your job) is the single point of failure. Diversify your income streams. Have your primary salary, but also cultivate side hustles, rental income, interest, or dividends. 
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="learning-card">
        <div class="learning-title">4. The Player Auction = Market Value of Skills</div>
        <div class="learning-text">
            <strong>The Business:</strong> At the auction, players are valued based on scarcity and demand. A rare skill (like a fast-bowling all-rounder) commands a massive premium over generic skills.<br><br>
            <strong>Your Lesson:</strong> Your salary is determined by supply and demand, not just hard work. If anyone can do your job, your "auction price" will remain low. Upskill continuously, develop niche expertise, and position yourself where demand drastically exceeds supply.
        </div>
    </div>
    """, unsafe_allow_html=True)
