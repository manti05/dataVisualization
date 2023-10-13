import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Data Set : Country,Life expectancy males,Life expectancy females,Birth rate,Death rate
# Data set is sorted by highest male life expectancy


def create_life_expectancy_graph(data_file_param):
	# Read data from the specified file
	data = pd.read_csv(data_file_param)

	# Convert life expectancies to float
	data['Life expectancy males'] = data['Life expectancy males'].str.rstrip(' years').astype(float)
	data['Life expectancy females'] = data['Life expectancy females'].str.rstrip(' years').astype(float)

	# Sort the data
	top5_males = data.nlargest(5, 'Life expectancy males')
	bottom5_males = data.nsmallest(5, 'Life expectancy males')
	top5_females = data.nlargest(5, 'Life expectancy females')
	bottom5_females = data.nsmallest(5, 'Life expectancy females')

	# Create subplots for male and female life expectancies
	fig, axs = plt.subplots(2, 1, figsize=(14, 8))

	# Plot the top 5 and bottom 5 male life expectancies
	axs[0].bar(top5_males['Country'], top5_males['Life expectancy males'], label='Top 5 Male Expectancies', color='b')
	axs[0].bar(bottom5_males['Country'], bottom5_males['Life expectancy males'], label='Bottom 5 Male Expectancies', color='r', alpha=0.6)
	axs[0].set_title('Top 5 and Bottom 5 Male Life Expectancies')
	axs[0].set_ylabel('Life Expectancy (years)')

	# Plot the top 5 and bottom 5 female life expectancies
	axs[1].bar(top5_females['Country'], top5_females['Life expectancy females'], label='Top 5 Female Expectancies', color='g')
	axs[1].bar(bottom5_females['Country'], bottom5_females['Life expectancy females'], label='Bottom 5 Female Expectancies', color='m', alpha=0.6)
	axs[1].set_title('Top 5 and Bottom 5 Female Life Expectancies')
	axs[1].set_ylabel('Life Expectancy (years)')

	# Rotate x-axis labels for better readability
	plt.xticks(rotation=45, ha='right')

	# Show legend and adjust subplot layout
	axs[0].legend()
	axs[1].legend()
	plt.tight_layout()

	# Display the plot
	plt.show()


def create_male_life_expectancy_line_graph(data_file_param, top_n=10, figsize=(10, 6)):
	# Read data from the specified file
	data = pd.read_csv(data_file_param)

	# Convert life expectancies to float
	data['Life expectancy males'] = data['Life expectancy males'].str.rstrip(' years').astype(float)
	data['Life expectancy females'] = data['Life expectancy females'].str.rstrip(' years').astype(float)

	# Sort the data for top N countries with highest male life expectancy
	top_males = data.nlargest(top_n, 'Life expectancy males')
	top_females = data[data['Country'].isin(top_males['Country'])]

	# Sort the female data in the same order as male data
	top_females = top_females.set_index('Country').loc[top_males['Country']].reset_index()

	# Create a line graph
	plt.figure(figsize=figsize)

	plt.plot(top_males['Country'], top_males['Life expectancy males'], marker='o', label='Male Life Expectancy')
	plt.plot(top_males['Country'], top_females['Life expectancy females'], marker='s', label='Female Life Expectancy')

	plt.title(f'Top {top_n} Countries With Highest Male Life Expectancy: Male vs. Female Life Expectancy')
	plt.xlabel('Country')
	plt.ylabel('Life Expectancy (years)')

	plt.xticks(rotation=45, ha='right')
	plt.legend()

	plt.tight_layout()

	plt.show()


def create_female_life_expectancy_line_graph(data_file_param, top_n=10, figsize=(10, 6)):
	# Read data from the specified file
	data = pd.read_csv(data_file_param)

	# Convert life expectancies to float
	data['Life expectancy males'] = data['Life expectancy males'].str.rstrip(' years').astype(float)
	data['Life expectancy females'] = data['Life expectancy females'].str.rstrip(' years').astype(float)

	# Sort the data for top N countries with highest female life expectancy
	top_females = data.nlargest(top_n, 'Life expectancy females')
	top_males = data[data['Country'].isin(top_females['Country'])]

	# Sort the male data in the same order as female data
	top_males = top_males.set_index('Country').loc[top_females['Country']].reset_index()

	# Create a line graph
	plt.figure(figsize=figsize)

	plt.plot(top_females['Country'], top_females['Life expectancy females'], marker='o', label='Female Life Expectancy')
	plt.plot(top_females['Country'], top_males['Life expectancy males'], marker='s', label='Male Life Expectancy')

	plt.title(f'Top {top_n} Countries With Highest Female Life Expectancy: Female vs. Male Life Expectancy')
	plt.xlabel('Country')
	plt.ylabel('Life Expectancy (years)')

	plt.xticks(rotation=45, ha='right')
	plt.legend()

	plt.tight_layout()

	plt.show()


def create_grouped_bar_chart_sorted_by_male_life_expectancy(data_file_param, top_n=10, figsize=(10, 6)):
	# Read your data from the CSV file
	data = pd.read_csv(data_file_param)

	# Convert relevant columns to float
	data['Life expectancy males'] = data['Life expectancy males'].str.rstrip(' years').astype(float)
	data['Life expectancy females'] = data['Life expectancy females'].str.rstrip(' years').astype(float)
	data['Birth rate'] = data['Birth rate'].str.rstrip(' ‰').astype(float)
	data['Death rate'] = data['Death rate'].str.rstrip(' ‰').astype(float)

	# Choose the countries you want to display
	selected_countries = data['Country'].head(top_n)

	# Filter the data for the selected countries
	selected_data = data[data['Country'].isin(selected_countries)]

	# Set the positions and width for the bars
	bar_width = 0.2
	index = np.arange(len(selected_countries))

	# Create a grouped bar chart
	fig, ax = plt.subplots(figsize=figsize)

	# Plot bars for Life Expectancy, Birth Rate, and Death Rate
	ax.bar(index - bar_width, selected_data['Life expectancy males'], bar_width, label='Life Expectancy (Males)')
	ax.bar(index, selected_data['Life expectancy females'], bar_width, label='Life Expectancy (Females)')
	ax.bar(index + bar_width, selected_data['Birth rate'], bar_width, label='Birth Rate', color='g')
	ax.bar(index + 2 * bar_width, selected_data['Death rate'], bar_width, label='Death Rate', color='r')

	# Set the x-axis labels and title
	ax.set_xticks(index)
	ax.set_xticklabels(selected_countries, rotation=45, ha='right')
	ax.set_xlabel('Country')
	ax.set_ylabel('Values')
	ax.set_title('Life Expectancy, Birth Rate, and Death Rate by Country')

	# Show legend
	ax.legend()

	# Show the grouped bar chart
	plt.tight_layout()
	plt.show()


def create_grouped_bar_chart_sorted_by_death_rate(data_file_param, top_n=10, figsize=(10, 6)):
	# Read your data from the CSV file
	data = pd.read_csv(data_file_param)

	# Convert relevant columns to float
	data['Life expectancy males'] = data['Life expectancy males'].str.rstrip(' years').astype(float)
	data['Life expectancy females'] = data['Life expectancy females'].str.rstrip(' years').astype(float)
	data['Birth rate'] = data['Birth rate'].str.rstrip(' ‰').astype(float)
	data['Death rate'] = data['Death rate'].str.rstrip(' ‰').astype(float)

	# Sort the data by the top N countries with the highest death rates
	sorted_data = data.nlargest(top_n, 'Death rate')

	# Set the positions and width for the bars
	bar_width = 0.2
	index = np.arange(len(sorted_data))

	# Create a grouped bar chart
	fig, ax = plt.subplots(figsize=figsize)

	# Plot bars for Life Expectancy (Males and Females), Birth Rate, and Death Rate
	ax.bar(index - bar_width, sorted_data['Life expectancy males'], bar_width, label='Life Expectancy (Males)')
	ax.bar(index, sorted_data['Life expectancy females'], bar_width, label='Life Expectancy (Females)')
	ax.bar(index + bar_width, sorted_data['Birth rate'], bar_width, label='Birth Rate', color='g')
	ax.bar(index + 2 * bar_width, sorted_data['Death rate'], bar_width, label='Death Rate', color='r')

	# Set the x-axis labels and title
	ax.set_xticks(index)
	ax.set_xticklabels(sorted_data['Country'], rotation=45, ha='right')
	ax.set_xlabel('Country')
	ax.set_ylabel('Values')
	ax.set_title(f'Top {top_n} Countries with Highest Death Rates')

	# Show legend
	ax.legend()

	# Show the grouped bar chart
	plt.tight_layout()
	plt.show()


def create_grouped_bar_chart_sorted_by_birth_rate(data_file_param, top_n=10, figsize=(10, 6)):
	# Read your data from the CSV file
	data = pd.read_csv(data_file_param)

	# Convert relevant columns to float
	data['Life expectancy males'] = data['Life expectancy males'].str.rstrip(' years').astype(float)
	data['Life expectancy females'] = data['Life expectancy females'].str.rstrip(' years').astype(float)
	data['Birth rate'] = data['Birth rate'].str.rstrip(' ‰').astype(float)
	data['Death rate'] = data['Death rate'].str.rstrip(' ‰').astype(float)

	# Sort the data by the top N countries with the highest birth rates
	sorted_data = data.nlargest(top_n, 'Birth rate')

	# Set the positions and width for the bars
	bar_width = 0.2
	index = np.arange(len(sorted_data))

	# Create a grouped bar chart
	fig, ax = plt.subplots(figsize=figsize)

	# Plot bars for Life Expectancy (Males and Females), Birth Rate, and Death Rate
	ax.bar(index - bar_width, sorted_data['Life expectancy males'], bar_width, label='Life Expectancy (Males)')
	ax.bar(index, sorted_data['Life expectancy females'], bar_width, label='Life Expectancy (Females)')
	ax.bar(index + bar_width, sorted_data['Birth rate'], bar_width, label='Birth Rate', color='g')
	ax.bar(index + 2 * bar_width, sorted_data['Death rate'], bar_width, label='Death Rate', color='r')

	# Set the x-axis labels and title
	ax.set_xticks(index)
	ax.set_xticklabels(sorted_data['Country'], rotation=45, ha='right')
	ax.set_xlabel('Country')
	ax.set_ylabel('Values')
	ax.set_title(f'Top {top_n} Countries with Highest Birth Rates')

	# Show legend
	ax.legend()

	# Show the grouped bar chart
	plt.tight_layout()
	plt.show()


# Create a dictionary to map graph types to functions
graph_functions = {
	"Life Expectancy Graph": create_life_expectancy_graph,
	"Male Life Expectancy Line Graph": create_male_life_expectancy_line_graph,
	"Female Life Expectancy Line Graph": create_female_life_expectancy_line_graph,
	"Grouped Bar Chart - Male Life Expectancy": create_grouped_bar_chart_sorted_by_male_life_expectancy,
	"Grouped Bar Chart - Death Rate": create_grouped_bar_chart_sorted_by_death_rate,
	"Grouped Bar Chart - Birth Rate": create_grouped_bar_chart_sorted_by_birth_rate,
}


# Modify the select_and_create_graph function
def select_and_create_graph(data_file_param, top_n=10, figsize=(10, 6)):
	while True:
		print("\nAvailable graph types:")

		# Display numbered options
		for i, graph_type in enumerate(graph_functions.keys(), 1):
			print(f"{i}. {graph_type}")

		try:
			# Take user input as an integer
			choice = int(input("\nEnter the number of the graph type you want to create or 0 to exit: "))

			if choice == 0:
				print("Exiting the program.")
				break

			# Check if the choice is within a valid range
			if choice < 1 or choice > len(graph_functions):
				print("\nInvalid choice. Please enter a number within the valid range.")
				continue

			# Get the selected graph type based on the user's choice
			selected_graph_type = list(graph_functions.keys())[choice - 1]

			# Call the corresponding function
			selected_function = graph_functions[selected_graph_type]
			if selected_function == create_life_expectancy_graph:
				selected_function(data_file_param)
			else:
				selected_function(data_file, top_n, figsize)

		except ValueError:
			print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
	# Code inside this block will only execute if the script is run directly
	data_file = "Life_expectancy.csv"
	select_and_create_graph(data_file, top_n=10)
