import streamlit as st
import dataseperation
import allfunctions
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
import seaborn as sns



# Add titles with specified Markdown for styling
st.sidebar.markdown("<h1 style='color: #FFD700; font-weight: bold; font-size: 48px; font-family: Arial, sans-serif;'>Welcome to WhatsInsights !!</h1>", unsafe_allow_html=True)
st.sidebar.header("Decode Conversations Creatively")

# Add a local image to your Streamlit app with a specified width
local_image_path = "/Users/maazaamir46/Desktop/intro.jpg"  # Replace with the path to your local image

# Set the desired width
width = 750

# Use st.image to display the local image with the specified width
st.image(local_image_path, caption='WhatsInsights.inc', width=width, use_column_width=True)

# Set the title with yellow color
st.markdown(
    '<h2 style="color: yellow; text-align: center; font-size: 36px;"> Need help exporting chat from WhatsApp? 💬</h2>'
    '<p style="color: white; text-align: center; font-size: 28px;">Follow the steps below:</p>',
    unsafe_allow_html=True
)



local_image_path = "/Users/maazaamir46/Desktop/guide2.jpg"  # Replace with the path to your local image

# Set the desired width
width = 750

# Use st.image to display the local image with the specified width
st.image(local_image_path, caption='WhatsInsights.inc', width=width, use_column_width=True)

local_image_path = "/Users/maazaamir46/Desktop/guide1.jpg"  # Replace with the path to your local image

# Set the desired width
width = 750

# Use st.image to display the local image with the specified width
st.image(local_image_path, caption='WhatsInsights.inc', width=width, use_column_width=True)


uploaded_file = st.sidebar.file_uploader("Choose an exported chat file to analyse !!")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    # st.text(data)
    df = dataseperation.preprocess(data)

    st.dataframe(df)

    # fetch unique users
    user_list = df['user'].unique().tolist()

    # Check if 'group_notification' is in the list before removing it
    if 'group_notification' in user_list:
        user_list.remove('group_notification')

    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)



#
    if st.sidebar.button("Lets Analyse with WhatsInsights"):
        pass
#         # Stats Area


        # Fetch statistics
        num_messages, words, num_media_messages, num_links = allfunctions.fetch_stats(selected_user, df)

        # Title for the statistics section
        st.markdown("""
            <h1 style="
                color: yellow;
                text-align: center;
                font-size: 44px;
                font-weight: bold;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
                animation: pulse 2s infinite;
            ">Here are Your Statistics</h1>
            <style>
                @keyframes pulse {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.05); }
                    100% { transform: scale(1); }
                }
            </style>
        """, unsafe_allow_html=True)

        # Define the column layout
        col1, col2, col3, col4 = st.columns(4)

        # Style for headers and values
        header_style = 'font-size: 20px; color: yellow; font-weight: bold; text-align: center;'
        value_style = 'font-size: 24px; color: white; font-weight: bold; text-align: center;'

        # Place statistics in columns
        with col1:
            st.markdown(f'<h2 style="{header_style}">📩 Total Messages</h2>', unsafe_allow_html=True)
            st.markdown(f'<h3 style="{value_style}">{num_messages}</h3>', unsafe_allow_html=True)

        with col2:
            st.markdown(f'<h2 style="{header_style}">📝 Total Words</h2>', unsafe_allow_html=True)
            st.markdown(f'<h3 style="{value_style}">{words}</h3>', unsafe_allow_html=True)

        with col3:
            st.markdown(f'<h2 style="{header_style}">📸 Media Shared</h2>', unsafe_allow_html=True)
            st.markdown(f'<h3 style="{value_style}">{num_media_messages}</h3>', unsafe_allow_html=True)

        with col4:
            st.markdown(f'<h2 style="{header_style}">🔗 Links Shared</h2>', unsafe_allow_html=True)
            st.markdown(f'<h3 style="{value_style}">{num_links}</h3>', unsafe_allow_html=True)

        # Monthly timeline
        # FEATURE 1

        # Heading for the Monthly Timeline
        st.markdown('<h1 style="color: yellow; text-align: center;">Your Timeline Over Months</h1>',
                    unsafe_allow_html=True)

        # Load the monthly timeline data
        timeline = allfunctions.monthly_timeline(selected_user, df)

        # Create the plot
        fig, ax = plt.subplots(figsize=(12, 6))  # Adjust size as needed

        # Plotting the data
        ax.plot(timeline['time'], timeline['message'], color='dodgerblue', linestyle='-', marker='o', linewidth=2,
                markersize=6)  # Enhanced style

        # Customize plot appearance
        plt.xticks(rotation=45)
        plt.xlabel('Month')
        plt.ylabel('Messages')
        plt.title('Monthly Chat Activity')
        plt.grid(True, linestyle='--', alpha=0.7)

        # Add a styled subheading with emojis
        st.markdown(
            '<p style="color: white; font-size: 24px; text-align: center;">'
            '📊 Here’s a look at how your chat activity has evolved month by month. 🌟'
            '</p>',
            unsafe_allow_html=True
        )

        # Display the plot
        st.pyplot(fig, clear_figure=True)

        # DAILY TIMELINE
        # FEATURE 2

        st.markdown('<h1 style="color: yellow; text-align: center;">Your Daily Timeline</h1>', unsafe_allow_html=True)

        # Load the daily timeline data
        daily_timeline = allfunctions.daily_timeline(selected_user, df)

        # Convert the 'only_date' column to datetime if it's not already
        daily_timeline['only_date'] = pd.to_datetime(daily_timeline['only_date'])

        # Filter data from April 2022 to the present
        start_date = datetime(2022, 4, 1)
        end_date = datetime.now()
        filtered_timeline = daily_timeline[
            (daily_timeline['only_date'] >= start_date) & (daily_timeline['only_date'] <= end_date)]

        # Create the plot
        fig, ax = plt.subplots(figsize=(12, 6))  # Adjust size as needed
        ax.plot(filtered_timeline['only_date'], filtered_timeline['message'], color='black')
        plt.xticks(rotation=45)
        plt.xlabel('Date')
        plt.ylabel('Messages')
        plt.title('Daily Chat Activity')
        plt.grid(True)

        # Add a styled sentence below the heading with emojis
        st.markdown(
            '<p style="color: white; font-size: 24px; text-align: center;">'
            '📅 Here is how your chat activity has looked over time. 📈'
            '</p>',
            unsafe_allow_html=True
        )

        # Display the plot
        st.pyplot(fig, clear_figure=True)


        # ACTIVITY MAP
        # FEATURE 3


        # Title for the overall activity map
        st.markdown("""
            <h1 style="
                color: yellow;
                text-align: center;
                font-size: 40px;
                font-weight: bold;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            ">Activity Map</h1>
        """, unsafe_allow_html=True)

        # Container for Busiest Day and Busiest Month
        with st.container():
            # Busiest Day Plot
            st.markdown("""
                <h2 style="
                    color: yellow;
                    text-align: center;
                    font-size: 32px;
                    font-weight: bold;
                    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
                ">📅 Busiest Day !!</h2>
                <p style="
                    color: white;
                    font-size: 18px;
                    text-align: center;
                    font-weight: normal;
                    margin-bottom: 20px;
                ">This graph gives you an idea of the day when you were most active. 🔥📈</p>
            """, unsafe_allow_html=True)

            busy_day = allfunctions.week_activity_map(selected_user, df)
            fig, ax = plt.subplots(figsize=(12, 8))  # Larger size for better visibility
            ax.barh(busy_day.index, busy_day.values, color='purple', edgecolor='black', alpha=0.8)  # Enhanced style
            plt.xlabel('Activity', fontsize=14, color='black')  # Changed to black for readability
            plt.ylabel('Day', fontsize=14, color='black')  # Changed to black for readability
            plt.title('Busiest Day', fontsize=16, color='black')  # Changed to black for readability
            plt.grid(axis='x', linestyle='--', alpha=0.5)
            plt.gca().invert_yaxis()  # Optional: Invert y-axis to show the highest value on top
            st.pyplot(fig, clear_figure=True)

            # Busiest Month Plot
            st.markdown("""
                <h2 style="
                    color: yellow;
                    text-align: center;
                    font-size: 32px;
                    font-weight: bold;
                    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
                ">📊 Busiest Month !!</h2>
                <p style="
                    color: while;
                    font-size: 18px;
                    text-align: center;
                    font-weight: normal;
                    margin-bottom: 20px;
                ">This graph shows you the month with the highest activity levels. 🌟📊</p>
            """, unsafe_allow_html=True)

            busy_month = allfunctions.month_activity_map(selected_user, df)
            fig, ax = plt.subplots(figsize=(12, 8))  # Larger size for better visibility
            ax.barh(busy_month.index, busy_month.values, color='orange', edgecolor='black', alpha=0.8)  # Enhanced style
            plt.xlabel('Activity', fontsize=14, color='black')  # Changed to black for readability
            plt.ylabel('Month', fontsize=14, color='black')  # Changed to black for readability
            plt.title('Busiest Month', fontsize=16, color='black')  # Changed to black for readability
            plt.grid(axis='x', linestyle='--', alpha=0.5)
            plt.gca().invert_yaxis()  # Optional: Invert y-axis to show the highest value on top
            st.pyplot(fig, clear_figure=True)


        import matplotlib.pyplot as plt
        from wordcloud import WordCloud
        import streamlit as st
        import numpy as np
        import pandas as pd

        # Ensure you have the function definition for `allfunctions.most_busy_users` and other dependencies.

        if selected_user == 'Overall':
            st.markdown('<h1 style="color: yellow; text-align: center;">🌟 Major Contributors !! 🌟</h1>',
                        unsafe_allow_html=True)

            x, new_df = allfunctions.most_busy_users(df)

            # Rename columns of the DataFrame
            new_df = new_df.rename(columns={new_df.columns[0]: 'Group Member', new_df.columns[1]: 'Percentage'})

            # Create a larger pie chart
            fig, ax = plt.subplots(figsize=(14, 10))  # Increased size for better visibility

            # Dark color scheme for pie chart
            num_segments = len(x)
            colors = plt.cm.Dark2(np.linspace(0, 1, num_segments))  # Use 'Dark2' colormap for distinct dark colors

            explode = [0.1 if i < 3 else 0 for i in range(num_segments)]

            wedges, texts, autotexts = ax.pie(
                x.values,
                labels=x.index,
                autopct='%1.1f%%',
                colors=colors,
                startangle=140,
                explode=explode,
                shadow=True
            )

            # Customize the appearance of labels and percentages
            for text in texts:
                text.set_fontsize(12)
                text.set_color('white')  # Use white color for better contrast on dark colors
                text.set_fontweight('bold')
            for autotext in autotexts:
                autotext.set_fontsize(10)
                autotext.set_color('white')
                autotext.set_fontweight('bold')

            ax.set_title('Contribution Distribution', fontsize=24, color='Red', pad=20)
            ax.legend(loc="best", fontsize='small', shadow=True, frameon=False)  # Add a legend

            # Display the pie chart
            st.pyplot(fig, clear_figure=True)

            # Display the DataFrame below the pie chart
            st.markdown('<h2 style="color: yellow; text-align: center;">📊 Detailed Contributor Data 📊</h2>',
                        unsafe_allow_html=True)
            st.markdown(
                '<p style="color: white; text-align: center; font-size: 18px; margin-bottom: 20px;">Here’s a detailed list of contributors and their respective activity levels. 🌟📈</p>',
                unsafe_allow_html=True)

            # Adjust DataFrame width and styling
            st.markdown("""
            <style>
            .dataframe-container {
                width: 100% !important;
            }
            .dataframe-container .dataframe {
                width: 100% !important;
            }
            .dataframe-container .dataframe thead th {
                font-weight: bold;
            }
            </style>
            """, unsafe_allow_html=True)

            st.dataframe(
                new_df.style.set_properties(**{
                    'background-color': 'black',
                    'color': 'white'
                }).set_table_styles([{
                    'selector': 'thead th',
                    'props': [('background-color', 'yellow'), ('color', 'black'), ('font-weight', 'bold')]
                }]),
                use_container_width=True
            )  # Use container width for the DataFrame

        # WordCloud
        import matplotlib.pyplot as plt
        from wordcloud import WordCloud
        import streamlit as st

        # Ensure you have the function definition for `allfunctions.create_wordcloud` and other dependencies.

        st.markdown('<h1 style="color: yellow; text-align: center;">🌟 Explore Your Word Cloud! 🌟</h1>',
                    unsafe_allow_html=True)

        df_wc = allfunctions.create_wordcloud(selected_user, df)

        # Enhance the WordCloud visualization
        fig, ax = plt.subplots(figsize=(10, 8))  # Increase figure size for better visibility

        # Display the WordCloud
        ax.imshow(df_wc, interpolation='bilinear')
        ax.axis('off')  # Hide axes for a cleaner look

        # Add a background color to make the WordCloud stand out
        fig.patch.set_facecolor('black')  # Set figure background to black
        ax.set_facecolor('black')  # Set plot background to black

        # Set a transparent color for the WordCloud so the black background shows through
        df_wc.recolor(colormap='coolwarm')

        st.pyplot(fig, clear_figure=True)

        # Add a descriptive paragraph below the WordCloud
        st.markdown(
            '<p style="color: white; text-align: center; font-size: 18px; margin-bottom: 20px;">Here’s a visual representation of your most frequently used words. 🌈🔍 The larger the word, the more frequently it appears in your chats!</p>',
            unsafe_allow_html=True
        )

        # Most common words

        # Get the most common words
        most_common_df = allfunctions.most_common_words(selected_user, df)

        # Create the bar graph
        fig, ax = plt.subplots(figsize=(12, 8))  # Increase figure size for better visibility

        # Plot the horizontal bar graph
        bars = ax.barh(most_common_df[0], most_common_df[1], color='dodgerblue')  # Use an attractive color

        # Add gridlines for better readability
        ax.grid(axis='x', linestyle='--', alpha=0.7)

        # Add labels and title
        plt.xlabel('Frequency', fontsize=14, color='white')
        plt.ylabel('Words', fontsize=14, color='white')
        plt.title('Most Common Words', fontsize=18, color='yellow')

        # Add text labels on the bars
        for bar in bars:
            width = bar.get_width()
            ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width}',
                    va='center', ha='left', color='white', fontsize=12)

        # Adjust tick labels
        plt.xticks(color='white')
        plt.yticks(color='white')

        # Set background color for the plot
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')

        # Display the plot
        st.markdown('<h1 style="color: yellow; text-align: center;">🔍 Most Common Words 🔍</h1>', unsafe_allow_html=True)

        st.markdown(
            '<p style="color: white; text-align: center; font-size: 18px; margin-bottom: 20px;">Here’s a breakdown of the most frequently used words in your chats. 📈🔤 The longer the bar, the more common the word!</p>',
            unsafe_allow_html=True)

        st.pyplot(fig, clear_figure=True)

        # Emoji analysis
        import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np
        import streamlit as st

        # Ensure you have the function definition for `allfunctions.emoji_helper` and other dependencies.

        emoji_df = allfunctions.emoji_helper(selected_user, df)

        # Check if the DataFrame is empty
        if emoji_df.empty:
            st.markdown('<h2 style="color: white; text-align: center;">No emojis were used in your chats. 📉</h2>',
                        unsafe_allow_html=True)
        else:
            # Print the column names for debugging
            st.write("Column names in emoji_df:", emoji_df.columns)

            # Rename columns to ensure consistency
            if len(emoji_df.columns) >= 2:
                emoji_df.columns = ['Emoji', 'Frequency']
            else:
                # Handle cases with unexpected number of columns
                st.write("Unexpected column names in emoji_df:", emoji_df.columns)
                if len(emoji_df.columns) > 0:
                    emoji_df = emoji_df.rename(columns={emoji_df.columns[0]: 'Emoji'})
                if len(emoji_df.columns) > 1:
                    emoji_df = emoji_df.rename(columns={emoji_df.columns[1]: 'Frequency'})
                else:
                    st.write("Not enough columns to rename.")
                    st.markdown('<h2 style="color: white; text-align: center;">Unable to process emoji data. 📉</h2>',
                                unsafe_allow_html=True)
                    st.stop()

            # Define the number of top emojis for the pie chart
            top_n = 6
            top_emoji_df = emoji_df.sort_values(by='Frequency', ascending=False).head(top_n)

            # Set up the layout with pie chart on top and list below
            st.markdown('<h1 style="color: yellow; text-align: center;">How Your Folks Play with Emojis! 🎉</h1>',
                        unsafe_allow_html=True)


            # Display the DataFrame below the pie chart
            st.markdown('<h2 style="color: yellow; text-align: center;">📊 Emoji Frequency Data 📊</h2>',
                        unsafe_allow_html=True)
            st.markdown(
                '<p style="color: white; text-align: center; font-size: 18px; margin-bottom: 20px;">Here’s a breakdown of how emojis are used in your chats. 🌟📈 The larger the slice, the more frequent the emoji!</p>',
                unsafe_allow_html=True)

            # Adjust DataFrame width and remove index column
            st.markdown("""
            <style>
            .dataframe-container {
                width: 100% !important;
            }
            .dataframe-container .dataframe {
                width: 100% !important;
            }
            .dataframe-container .dataframe thead th {
                font-weight: bold;
            }
            </style>
            """, unsafe_allow_html=True)

            # Remove the index column and style the DataFrame
            st.dataframe(
                emoji_df.style.set_properties(**{
                    'background-color': 'black',
                    'color': 'white'
                }).set_table_styles([{
                    'selector': 'thead th',
                    'props': [('background-color', 'yellow'), ('color', 'black'), ('font-weight', 'bold')]
                }]).hide(axis='index'),  # Hide index column
                use_container_width=True
            )  # Use container width for the DataFrame
