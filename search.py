import streamlit as st
import folium
from streamlit_folium import st_folium

# Shops data
shops = [
    {
        "name": "Occasion Technology Shop",
        "latitude": -1.940278,
        "longitude": 30.060556,
        "description": "Sells and buys used electronic devices.",
        "phone": "+250 728 294 682",
        "address": "12 KN 121 Street",
        "price_ranges": "rwf 1200 - 5000"
    },
    {
        "name": "ElectroHub",
        "latitude": -1.950278,
        "longitude": 30.070556,
        "description": "Specializes in new and used electronic devices.",
        "phone": "+250 728 123 456",
        "address": "45 KG 14 Ave",
        "price_ranges": "rwf 2000 - 15000"
    },
    {
        "name": "TechMart",
        "latitude": -1.960278,
        "longitude": 30.080556,
        "description": "Offers a wide range of electronic gadgets.",
        "phone": "+250 728 789 012",
        "address": "89 KK 23 Rd",
        "price_ranges": "rwf 3000 - 20000"
    }
]

# Layout with two columns
col1, col2 = st.columns([1, 2])

# User Interaction Section in col1
with col1:
    st.markdown("""
        <div style='text-align: left; background-color: lightgreen; border-radius: 5px; padding: 5px;'>
            <h3 style='color: blue;'>Electronic Repair Search Gate</h3>
        </div>
    """, unsafe_allow_html=True)
    st.subheader("We Help you to get the best Service")
with col2:
    # User input
    service = st.selectbox(
        "Select the service you want that best fit your search:",
        ["Repair phone", "Repair Television", "Repair charger", "Repair refrigerator", "Repair Generator", "Repair Laptop",
         "Repair Desktop"]
    )

    budget = st.number_input("Enter your budget (Min of RWF100):", min_value=0, step=100)
    payment_method = st.radio("To Optimize your Search, Tell us How do you want to pay?", ["Cash", "Card", "Momo","Bank Tranfer"])
    vip_service = st.checkbox("Do you want a home service?")

    # Placeholder for the results
    result_placeholder = st.empty()

    # Find the best shop based on criteria
    if st.button("Find the best shop"):
        # Filter shops based on criteria
        filtered_shops = [
            shop for shop in shops
            if int(shop["price_ranges"].split("-")[0].strip('rwf ')) <= budget
        ]

        if filtered_shops:
            best_shop = filtered_shops[0]
            result_placeholder.success(f"Beased on your Input, The best shop for your needs is {best_shop['name']}.")
            st.write(f"**Description:** {best_shop['description']}")
            st.write(f"**Phone:** {best_shop['phone']}")
            st.write(f"**Address:** {best_shop['address']}")
            st.write(f"**Price Range:** {best_shop['price_ranges']}")
        else:
            result_placeholder.error("No shop matches your criteria. Try adjusting your search.")

        # Trigger map update in col2
        st.session_state["selected_shop"] = best_shop if filtered_shops else None

# Map Display Section in col2
with col1, col2:
    if "selected_shop" in st.session_state and st.session_state["selected_shop"]:
        best_shop = st.session_state["selected_shop"]
        # Create a map
        shop_map = folium.Map(location=[best_shop["latitude"], best_shop["longitude"]], zoom_start=15)
        folium.Marker(
            [best_shop["latitude"], best_shop["longitude"]],
            popup=f"{best_shop['name']} - {best_shop['address']}",
            tooltip=best_shop['name']
        ).add_to(shop_map)

        # Display the map
        st_folium(shop_map, width=700, height=500)
    else:
        st.info("Map will display here once you find a shop.The Map will Guide you to the Shop")
