# -*- coding: utf-8 -*-
"""capstone.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bjNptPnytH4z2rYPPnv65q9iMGxuhq8d
"""

# Commented out IPython magic to ensure Python compatibility.
# %load_ext sql

# Commented out IPython magic to ensure Python compatibility.
# %sql sqlite:///uni_db

# Commented out IPython magic to ensure Python compatibility.
# %%sql
#   CREATE TABLE university_details(
#           id_number INT,
#           university_name VARCHAR(40),
#           state VARCHAR(40),
#           PRIMARY KEY(id_number)
#         )
# 
#

# Commented out IPython magic to ensure Python compatibility.
# %%sql CREATE TABLE tuition_cost(
#            id_number INT,
#             state_code VARCHAR (30),
#            type VARCHAR (40),
#            degree_length VARCHAR (10),
#             room_and_board DOUBLE,
#             in_state_tuition DOUBLE,
#             in_state_total DOUBLE,
#             out_of_state_tuition DOUBLE,
#             out_of_state_total DOUBLE,
#             PRIMARY KEY(id_number),
#             FOREIGN KEY (id_number) REFERENCES university_details(id_number)
#         )
#

# Commented out IPython magic to ensure Python compatibility.
# %%sql CREATE TABLE tuition_income(
#            id_number INT,
#            total_price DOUBLE,
#             year DOUBLE,
#           campus VARCHAR (40),
#            net_cost DOUBLE,
#             income_lvl VARCHAR (30),
#            PRIMARY KEY(id_number,year),
#             FOREIGN KEY (id_number) REFERENCES university_details(id_number)
#         )
#

# Commented out IPython magic to ensure Python compatibility.
# %%sql CREATE TABLE salary_potential(
#           id_number INT,
#           rank DOUBLE,
#           early_career_pay DOUBLE,
#           mid_career_pay DOUBLE,
#           make_world_better_percent DOUBLE,
#           stem_percent DOUBLE,
#          PRIMARY KEY(id_number),
#            FOREIGN KEY (id_number) REFERENCES university_details(id_number)
#         )
#

# Commented out IPython magic to ensure Python compatibility.

#  %%sql CREATE TABLE historical_tuition(
           type VARCHAR (40),
          year VARCHAR (30),
            tuition_type VARCHAR (30),
           tuition_cost DOUBLE,
            PRIMARY KEY(type,year),
            FOREIGN KEY (type) REFERENCES tuition_cost(type)
        )

# Commented out IPython magic to ensure Python compatibility.
# %%sql
# insert into university_details(id_number,university_name,state )values
#  (011, 'Aaniiih Nakoda College', 'Montana'),
#   (012, 'Abilene Christian University', 'Texas'),
#   (013, 'Abraham Baldwin Agricultural College','Georgia')

# Commented out IPython magic to ensure Python compatibility.
# %%sql INSERT INTO tuition_cost (id_number, state_code, type, degree_length, room_and_board, in_state_tuition, in_state_total, out_of_state_tuition, out_of_state_total)values
# 
#  (7, 'NY', 'Private', 4, 16030, 38660, 54690, 38660, 54690),
#     (8, 'NY', 'Public', 2, 11660, 5375, 17035, 9935, 21595),
#     (9, 'MI', 'Private', 4, 11318, 37087, 48405, 37087, 48405)

# Commented out IPython magic to ensure Python compatibility.
# %%sql INSERT INTO tuition_income (id_number, total_price, year, campus, net_cost, income_lvl) VALUES
# (001, 20174, 2016, 'On Campus', 11475, '0 to 30,000'),
# (002, 22413, 2017, 'Off Campus', 0, '0 to 30,000'),
# (003, 39475, 2017, 'Off Campus', 0, '0 to 30,000')

# Commented out IPython magic to ensure Python compatibility.
# %%sql INSERT INTO salary_potential (id_number, rank, early_career_pay, mid_career_pay, make_world_better_percent, stem_percent)VALUES
#     (011, 1, 54400, 104500, 51, 31),
#     (012, 2, 57500, 103900, 59, 45),
#    (013, 3, 52300, 97400, 50, 15),
#     (014, 4, 54500, 93500, 61, 30)
#

# Commented out IPython magic to ensure Python compatibility.
# %%sql INSERT INTO historical_tuition (type, year, tuition_type, tuition_cost) VALUES
#         ('All Institutions','1985-86','All Constant',10893),
#         ('Public','1985-86','All Constant',7964),
#         ('Private','1985-86','All Constant',19812)

# Commented out IPython magic to ensure Python compatibility.
# %%sql
# select * from university_details

# Commented out IPython magic to ensure Python compatibility.
# %%sql
# select * from tuition_cost

# Commented out IPython magic to ensure Python compatibility.
# %%sql
# select * from tuition_income

# Commented out IPython magic to ensure Python compatibility.
# %%sql
# select * from salary_potential



# Commented out IPython magic to ensure Python compatibility.
# %%sql
# select * from historical_tuition