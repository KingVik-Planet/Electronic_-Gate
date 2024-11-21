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
        "price_ranges": "rwf 1000 - 2000"
    },
    {
        "name": "ElectroHub",
        "latitude": -1.950278,
        "longitude": 30.070556,
        "description": "Specializes in new and used electronic devices.",
        "phone": "+250 728 123 456",
        "address": "45 KG 14 Ave",
        "price_ranges": "rwf 2000 - 4000"
    },
    {
        "name": "TechMart",
        "latitude": -1.960278,
        "longitude": 30.080556,
        "description": "Offers a wide range of electronic gadgets.",
        "phone": "+250 728 789 012",
        "address": "89 KK 23 Rd",
        "price_ranges": "rwf 3000 - 7000"
    },
    {
        "name": "Techno Technical Repair Shop",
        "latitude": -1.960279,
        "longitude": 30.090556,
        "description": "Sells phone accessories.",
        "phone": "+250 727 391 943",
        "address": "50 KK 15 Rd",
        "price_ranges": "rwf 6500 -10000 "
    },
    {
        "name": "electronics_repair",
        "latitude": -1.960278,
        "longitude": 30.080606,
        "description": "Sells second hand computers.",
        "phone": "+250 728 789 012",
        "address": "70 KN 10 Rd",
        "price_ranges": "rwf 9000 - 13000"
    },
    {
        "name": "Fis Repair Shop",
        "latitude": -1.960278,
        "longitude": 30.080706,
        "description": "Sells computers and accessories.",
        "phone": "+250 722 414 150",
        "address": "89 KG 45 Rd",
        "price_ranges": "rwf 13000 - 15000"
    },
    {
        "name": "Kitchen Electrics",
        "latitude": -1.960278,
        "longitude": 30.081156,
        "description": "Repairs computers.",
        "phone": "+250 734 324 103",
        "address": "92 KK 20 Rd",
        "price_ranges": "rwf 15000 - 20000"
    },
    {
        "name": "Kappo Tech",
        "latitude": -1.960278,
        "longitude": 30.082556,
        "description": "Repairs computers.",
        "phone": "+250 734 324 105",
        "address": "65 KG 45 Rd",
        "price_ranges": "rwf 20000 - 25000"
    },
    {
        "name": "FilosTech",
        "latitude": -1.960278,
        "longitude": 30.080560,
        "description": "We repair Digital TVs.",
        "phone": "+250 728 789 012",
        "address": "30 KN 70 Rd",
        "price_ranges": "rwf 24000 - 30000"
    },
    {
        "name": "BiremeraShop",
        "latitude": -1.960278,
        "longitude": 30.085556,
        "description": "we sell phone lcds, Bluetooth radio, Fridge repair, Charger Repair.",
        "phone": "+250 728 789 011",
        "address": "50 Kk 29 Rd",
        "price_ranges": "rwf 29000 - 50000"
    },
    {
        "name": "PhilosShop",
        "latitude": -1.960278,
        "longitude": 30.084556,
        "description": " Sells electronic devices.",
        "phone": "+250 786 200 749",
        "address": "10 KN 23 Rd",
        "price_ranges": "rwf 50000 - 1250000"
    }


]

# Initialize session state for search results
if "selected_shop" not in st.session_state:
    st.session_state["selected_shop"] = None

# Layout with two columns
col1, col2 = st.columns([1, 2])

# User Interaction Section in col1
with col1:
    st.markdown("""
        <div style='text-align: center; background-color: gray; border-radius: 5px; padding: 5px;'>
            <h1 style='color: black;'>Electronic Technical Repair Shop</h1>
        </div>
    """, unsafe_allow_html=True)
    st.subheader("We Help you to get the best Service")
    st.image("images/Electronic.jpg", width=345)

# User input section in col2
with col2:
    service = st.selectbox(
        "Select the service you want that best fit your search from the dropdown:",
        ["Repair phone", "Repair Television", "Repair charger", "Repair refrigerator", "Repair Generator", "Repair Laptop", "Repair Desktop"]
    )

    budget = st.number_input("Enter your budget (Min of RWF100):", min_value=0, step=500)
    # payment_method = st.radio("To Optimize your Search, Tell us How do you want to pay?", ["Cash", "Card", "Momo", "Bank Transfer"])
    vip_service = st.checkbox("Do you want a home service?")

    # Placeholder for the results
    result_placeholder = st.container()

    # Find the best shop based on criteria
    if st.button("Find the best shop"):
        # Filter shops based on criteria
        filtered_shops = [
            shop for shop in shops
            if int(shop["price_ranges"].split("-")[0].strip('rwf ')) <= budget <= int(shop["price_ranges"].split("-")[1].strip('rwf '))
        ]

        if filtered_shops:
            best_shop = filtered_shops[0]
            result_placeholder.success(f"Based on your input, the best shop for your needs is {best_shop['name']}.")
            st.write(f"**Name:** {best_shop['name']}")
            st.write(f"**Phone:** {best_shop['phone']}")
            st.write(f"**Address:** {best_shop['address']}")
            st.write(f"**Price Range:** {best_shop['price_ranges']}")
            st.session_state["selected_shop"] = best_shop
        else:
            result_placeholder.error("No shop matches your criteria. Try adjusting your search.")
            st.session_state["selected_shop"] = None

# Map Display Section in col2
if st.session_state["selected_shop"]:
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
    st.info("""
        Map will display here once we find a shop.
        The map will guide you to the shop.
    """)
