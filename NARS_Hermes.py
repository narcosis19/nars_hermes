import os
import streamlit as st
import streamlit.components.v1 as components

# ==============================================================================
# 0. STREAMLIT CONFIGURATION & CUSTOM STYLING (BLUE THEME)
# ==============================================================================
LOGO_PATH1 = os.path.join("images", "logo.ico")
LOGO_PATH2 = os.path.join("images", "logo.ico")
LOGO_PATH3 = os.path.join("images", "ericsson_w.png")
LOGO_PATH4 = os.path.join("images", "logo.ico")
#LOGO_PATH = """
# <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="28" height="28">
#   <path fill="#ffffff" d="M18.8 82.2l62.4-23.8c2.4-.9 3.6-3.6 2.7-6-.9-2.4-3.6-3.6-6-2.7L15.5 73.5c-2.4.9-3.6 3.6-2.7 6 .9 2.4 3.6 3.6 6 2.7zM18.8 56.6l62.4-23.8c2.4-.9 3.6-3.6 2.7-6-.9-2.4-3.6-3.6-6-2.7L15.5 47.9c-2.4.9-3.6 3.6-2.7 6 .9 2.4 3.6 3.6 6 2.7zM18.8 31.1l62.4-23.8c2.4-.9 3.6-3.6 2.7-6-.9-2.4-3.6-3.6-6-2.7L15.5 22.4c-2.4.9-3.6 3.6-2.7 6 .9 2.4 3.6 3.6 6 2.7z"/>
# </svg>
# """

st.set_page_config(
    page_title="Network Analytics & Reporting Suite",
    page_icon=LOGO_PATH1 if os.path.exists(LOGO_PATH1) else "📶",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Font Awesome for Microsoft / OneDrive Style UI Icons */
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

    :root {
        --primary-blue: #0078d4;
        --primary-blue-hover: #005a9e;
        --sidebar-bg: #faf9f8;
        --border-color: #b3d1ff;
        --text-primary: #003366;
        --text-secondary: #004080;
        --light-blue-bg: #eff6fc;
        --header-bg-gradient: linear-gradient(90deg, #004080 0%, #0078d4 100%);
    }

    /* Streamlit Global Primary Buttons & Login Buttons in Blue */
    div.stButton > button[kind="primary"],
    .stFormSubmitButton > button {
        background-color: var(--primary-blue) !important;
        border-color: var(--primary-blue) !important;
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    div.stButton > button[kind="primary"]:hover,
    .stFormSubmitButton > button:hover {
        background-color: var(--primary-blue-hover) !important;
        border-color: var(--primary-blue-hover) !important;
    }

    /* Login Form Input Fields Focus Highlight in Blue */
    .stTextInput input:focus {
        border-color: var(--primary-blue) !important;
        box-shadow: 0 0 0 1px var(--primary-blue) !important;
    }

    /* Hide standard Streamlit header and reduce top padding */
    header[data-testid="stHeader"] {
        background-color: transparent;
        z-index: 100000;
    }
    
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
    }

    .brand {
        display: flex;
        align-items: center;
        font-weight: 600;
        font-size: 16px;
        color: #ffffff !important; /* White color for contrast against blue header */
        text-decoration: none;
    }

    /* Shades of Blue Header Bar - No Border Lines */
    div[data-testid="stHorizontalBlock"]:has(.brand) {
        background: var(--header-bg-gradient) !important;
        padding: 8px 16px !important;
        border: none !important;
        border-bottom: none !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1) !important;
        margin-bottom: 1rem;
        border-radius: 6px;
        display: flex !important;
        align-items: center !important;
    }

    /* Force all inner column wrappers (col_left, col_right) to inherit header background with no borders */
    div[data-testid="stHorizontalBlock"]:has(.brand) > div[data-testid="column"] {
        display: flex !important;
        align-items: center !important;
        background: inherit !important;
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
    }

    /* Ensure child inner horizontal blocks inside col_left/col_right also inherit background & stay borderless */
    div[data-testid="stHorizontalBlock"]:has(.brand) div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        align-items: center !important;
        width: 100%;
        background: inherit !important;
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
    }

    /* Vertically center user text container */
    .user-display-container {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        height: 100%;
        width: 100%;
        font-size: 13px;
        color: #ffffff !important; /* White color for visibility */
        white-space: nowrap;
    }

    /* Position Sidebar below Header */
    [data-testid="stSidebar"] {
        top: 60px !important;
        height: calc(100vh - 60px) !important;
        background-color: var(--sidebar-bg) !important;
        border-right: 1px solid var(--border-color);
    }
    
    [data-testid="stSidebar"] .block-container {
        padding-top: 1rem !important;
    }

    /* OneDrive / Blue Theme Dashboard Cards */
    .app-card {
        background-color: #ffffff;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 24px;
        text-align: center;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 1.6px 3.6px 0 rgba(0,120,212,0.08), 0 0.3px 0.9px 0 rgba(0,0,0,0.05);
        transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
        margin-bottom: 10px;
    }
    .app-card:hover {
        background-color: var(--light-blue-bg);
        box-shadow: 0 3.2px 7.2px 0 rgba(0,120,212,0.15), 0 0.6px 1.8px 0 rgba(0,0,0,0.1);
        border-color: var(--primary-blue);
    }
    .app-icon { font-size: 2.8rem; margin-bottom: 12px; }
    .app-title { font-weight: 600; font-size: 1.1rem; color: var(--text-primary); margin-bottom: 6px; }
    .app-desc { font-size: 0.85rem; color: var(--text-secondary); }
</style>
""", unsafe_allow_html=True)

# USER DATABASE
USERS_DB = {
    "esnanar": {
        "password": "0190nar", 
        "nickname": "Nar", 
        "apps": ["5g_kpi_processor", "4g_kpi_processor", "2g_kpi_processor", "weekly_ndo_db"]
    },
    "user1": {
        "password": "password1", 
        "nickname": "Alex", 
        "apps": ["5g_kpi_processor", "4g_kpi_processor", "2g_kpi_processor"]
    },
    "john_koi": {
        "password": "koi_john", 
        "nickname": "Koi", 
        "apps": ["weekly_ndo_db"]
    },
    "user3": {
        "password": "password3", 
        "nickname": "David", 
        "apps": ["others"]
    }
}

ALL_APPS = [
    {"id": "5g_kpi_processor", "title": "5G KPI Data Processor", "icon": "📶", "description": "Aggregate 5G performance counter data."},
    {"id": "4g_kpi_processor", "title": "4G KPI Data Processor", "icon": "📊", "description": "Aggregate 4G performance counter data."},
    {"id": "2g_kpi_processor", "title": "2G KPI Data Processor", "icon": "🗺️", "description": "Aggregate 2G performance counter data."},
    {"id": "weekly_ndo_db", "title": "Weekly NDO KPI Dashboard", "icon": "⚙️", "description": "Weekly NDO OSS KPI Performance."}
]

# Session State Initialization
if "authenticated" not in st.session_state: st.session_state.authenticated = False
if "user" not in st.session_state: st.session_state.user = None
if "nickname" not in st.session_state: st.session_state.nickname = None
if "allowed_apps" not in st.session_state: st.session_state.allowed_apps = []
if "current_app" not in st.session_state: st.session_state.current_app = "home"
if "click_tracker" not in st.session_state: st.session_state.click_tracker = {}

# Restore session state from query parameters on browser refresh
if not st.session_state.authenticated and "auth" in st.query_params and st.query_params["auth"] == "true":
    u = st.query_params.get("user")
    if u in USERS_DB:
        st.session_state.authenticated = True
        st.session_state.user = u
        st.session_state.nickname = USERS_DB[u].get("nickname", u)
        st.session_state.allowed_apps = USERS_DB[u]["apps"]
        st.session_state.current_app = st.query_params.get("app", "home")

def collapse_sidebar_if_home():
    """Helper to programmatically collapse the sidebar if we are on the Home page."""
    if st.session_state.current_app == "home":
        components.html("""
            <script>
                const streamlitDoc = window.parent.document;
                const sidebar = streamlitDoc.querySelector('[data-testid="stSidebar"]');
                if (sidebar && sidebar.getAttribute('aria-expanded') === 'true') {
                    const collapseBtn = streamlitDoc.querySelector('button[data-testid="collapsedControl"]');
                    if (collapseBtn) {
                        collapseBtn.click();
                    }
                }
            </script>
        """, height=0)

def expand_sidebar_if_module():
    """Helper to programmatically expand the sidebar when navigating to sub-modules."""
    if st.session_state.current_app != "home":
        components.html("""
            <script>
                const streamlitDoc = window.parent.document;
                const sidebar = streamlitDoc.querySelector('[data-testid="stSidebar"]');
                if (sidebar && sidebar.getAttribute('aria-expanded') === 'false') {
                    const expandBtn = streamlitDoc.querySelector('button[data-testid="collapsedControl"]');
                    if (expandBtn) {
                        expandBtn.click();
                    }
                }
            </script>
        """, height=0)

def render_login_page():
    col1, col2, col3 = st.columns([1, 1.3, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        c_logo, c_title = st.columns([0.2, 0.8])
        with c_logo:
            if os.path.exists(LOGO_PATH2): 
                st.image(LOGO_PATH2, width=60)
        with c_title:
            st.markdown("<h3 style='color: #0078d4; margin: 0;'>Network Analytics & Reporting Suite</h3>", unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.form("login_form"):
            username = st.text_input("Username").strip()
            password = st.text_input("Password", type="password").strip()
            submitted = st.form_submit_button("Sign In", type="primary", use_container_width=True)
            
            if submitted:
                if username in USERS_DB and USERS_DB[username]["password"] == password:
                    st.session_state.authenticated = True
                    st.session_state.user = username
                    st.session_state.nickname = USERS_DB[username].get("nickname", username)
                    st.session_state.allowed_apps = USERS_DB[username]["apps"]
                    st.session_state.current_app = "home"
                    
                    st.query_params["auth"] = "true"
                    st.query_params["user"] = username
                    st.query_params["app"] = "home"
                    st.rerun()
                else:
                    st.error("Invalid Username or Password")

def logout():
    st.session_state.authenticated = False
    st.session_state.user = None
    st.session_state.nickname = None
    st.session_state.allowed_apps = []
    st.session_state.current_app = "home"
    st.query_params.clear()
    st.rerun()

def render_header():
    """Renders top navigation bar header with Home, Logout, and User info on the right."""
    col_left, col_right = st.columns([3.2, 1.8])
    with col_left:
        c_logo, c_title = st.columns([0.05, 0.89])
        with c_logo:
            if os.path.exists(LOGO_PATH3):
                st.image(LOGO_PATH3, width=26)
        with c_title:
            st.markdown('<div class="brand" style="line-height: 1;">Network Analytics & Reporting Suite</div>', unsafe_allow_html=True)
            
    with col_right:
        sub_user, sub_home, sub_logout = st.columns([0.5, 0.25, 0.25])
        with sub_user:
            display_name = st.session_state.user or st.session_state.nickname
            st.markdown(f"<div class='user-display-container'>👤 <b>{display_name}</b></div>", unsafe_allow_html=True)
        with sub_home:
            if st.button("🏠 Home", key="header_home_btn", use_container_width=True):
                st.session_state.current_app = "home"
                st.query_params["app"] = "home"
                st.rerun()
        with sub_logout:
            if st.button("🚪 Logout", key="header_btn_logout", use_container_width=True):
                logout()

def render_sidebar():
    """Renders sidebar with the custom application logo at the top."""
    with st.sidebar:
        if os.path.exists(LOGO_PATH4):
            col_logo_space, col_logo_img, col_logo_right = st.columns([0.1, 0.9, 0.1])
            with col_logo_img:
                st.image(LOGO_PATH4, width=50)
            st.markdown("<br>", unsafe_allow_html=True)
            st.sidebar.markdown("---")

def render_home_page():
    st.markdown("### 🚀 Home")
    greeting_name = st.session_state.nickname or st.session_state.user
    st.markdown(f"<p style='color: #004080; margin-bottom: 20px;'>Hi {greeting_name}! Here are the available apps for you. Double-Click to open module.</p>", unsafe_allow_html=True)
    
    accessible_apps = [app for app in ALL_APPS if app["id"] in st.session_state.allowed_apps]
    
    if not accessible_apps:
        st.warning("⚠️ No applications assigned to your account.")
        return

    cols = st.columns(3)
    for idx, app_info in enumerate(accessible_apps):
        app_id = app_info["id"]
        with cols[idx % 3]:
            st.markdown(f"""
                <div class="app-card">
                    <div class="app-icon">{app_info['icon']}</div>
                    <div class="app-title">{app_info['title']}</div>
                    <div class="app-desc">{app_info['description']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            button_label = "Click again to launch" if st.session_state.click_tracker.get(app_id, False) else "Open Module"
            if st.button(f"{button_label} ▶", key=f"launch_{app_id}", use_container_width=True):
                if st.session_state.click_tracker.get(app_id, False):
                    st.session_state.click_tracker[app_id] = False
                    st.session_state.current_app = app_id
                    st.query_params["app"] = app_id
                    st.rerun()
                else:
                    st.session_state.click_tracker = {app_id: True}
                    st.toast(f"Click once more on '{app_info['title']}' to launch!")

# ==============================================================================
# MAIN CONTROLLER & ROUTER
# ==============================================================================
def main():
    if not st.session_state.authenticated:
        render_login_page()
    else:
        render_header()
        render_sidebar()
        
        current_app = st.session_state.current_app
        
        if current_app == "home":
            render_home_page()
            collapse_sidebar_if_home()
        else:
            expand_sidebar_if_module()
            # Dynamically import and run separate app files
            if current_app == "5g_kpi_processor":
                from apps.app_5g import run as run_app
            elif current_app == "4g_kpi_processor":
                from apps.app_4g import run as run_app
            elif current_app == "2g_kpi_processor":
                from apps.app_2g import run as run_app
            elif current_app == "weekly_ndo_db":
                from apps.app_ndo_db_wkly import run as run_app
            else:
                run_app = None

            if run_app:
                run_app()

if __name__ == "__main__":
    main()