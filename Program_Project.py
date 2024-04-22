# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:03:08 2024

@author: garre
"""


import streamlit as st

def calculate_averages(total_points, total_rebounds, total_assists, total_steals, total_blocks, total_turnovers, num_games):
    if num_games == 0:
        return None, None, None, None, None, None
    avg_points = total_points / num_games
    avg_rebounds = total_rebounds / num_games
    avg_assists = total_assists / num_games
    avg_steals = total_steals / num_games
    avg_blocks = total_blocks / num_games
    avg_turnovers = total_turnovers / num_games
    return avg_points, avg_rebounds, avg_assists, avg_steals, avg_blocks, avg_turnovers


def main():
    st.title("Basketball Player Averages Calculator")

    player_name = st.text_input("Enter a player's name:")
    num_games = st.number_input("Enter number of career games played:", min_value=0, step=1)

    if num_games == 0:
        st.write(f"\nPlayer: {player_name}")
        st.write(f"{player_name} has not played any games. There are no averages available.")
    else:
        total_points = st.number_input("Enter total points:", min_value=0, step=1)
        total_rebounds = st.number_input("Enter total rebounds:", min_value=0, step=1)
        total_assists = st.number_input("Enter total assists:", min_value=0, step=1)
        total_steals = st.number_input("Enter total steals:", min_value=0, step=1)
        total_blocks = st.number_input("Enter total blocks:", min_value=0, step=1)
        total_turnovers = st.number_input("Enter total turnovers:", min_value=0, step=1)

        avg_points, avg_rebounds, avg_assists, avg_steals, avg_blocks, avg_turnovers = calculate_averages(
            total_points, total_rebounds, total_assists, total_steals, total_blocks, total_turnovers, num_games)

        if avg_points is not None:
            st.write(f"\nPlayer: {player_name}")
            st.write(f"{player_name}'s averages for {num_games} career games:")
            st.write(f"- Points: {avg_points:.2f}")
            st.write(f"- Rebounds: {avg_rebounds:.2f}")
            st.write(f"- Assists: {avg_assists:.2f}")
            st.write(f"- Steals: {avg_steals:.2f}")
            st.write(f"- Blocks: {avg_blocks:.2f}")
            st.write(f"- Turnovers: {avg_turnovers:.2f}")
        else:
            st.write(f"\nPlayer: {player_name}")
            st.write(f"{player_name} has not played any games. No averages available.")

if __name__ == "__main__":
    main()
    
    
    