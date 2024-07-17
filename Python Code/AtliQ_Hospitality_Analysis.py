import pandas as pd

# Function to load data
def load_data(base_path):
    dim_date = pd.read_csv(f'{base_path}/dim_date.csv')
    dim_hotels = pd.read_csv(f'{base_path}/dim_hotels.csv')
    dim_rooms = pd.read_csv(f'{base_path}/dim_rooms.csv')
    fact_aggregated_bookings = pd.read_csv(f'{base_path}/fact_aggregated_bookings.csv')
    fact_bookings = pd.read_csv(f'{base_path}/fact_bookings.csv')
    
    return dim_date, dim_hotels, dim_rooms, fact_aggregated_bookings, fact_bookings

# Function to clean data
def clean_data(dim_date, dim_hotels, dim_rooms, fact_aggregated_bookings, fact_bookings):
    # Convert date columns to datetime
    dim_date['date'] = pd.to_datetime(dim_date['date'], format='%d-%b-%y')
    fact_bookings['booking_date'] = pd.to_datetime(fact_bookings['booking_date'], format='%d-%m-%Y')
    fact_bookings['checkout_date'] = pd.to_datetime(fact_bookings['checkout_date'], format='%d-%m-%Y')
    fact_bookings['check_in_date'] = pd.to_datetime(fact_bookings['check_in_date'], format='%d-%m-%Y')
    
    return dim_date, dim_hotels, dim_rooms, fact_aggregated_bookings, fact_bookings

# Function to analyze metrics
def analyze_metrics(fact_bookings, fact_aggregated_bookings):
    # Compute metrics
    revenue_generated = fact_bookings['revenue_generated'].sum()
    total_bookings = len(fact_bookings)
    average_rating = fact_bookings['ratings_given'].mean()
    total_capacity = fact_aggregated_bookings['capacity'].sum()
    total_successful_bookings = fact_aggregated_bookings['successful_bookings'].sum()
    occupancy_percentage = total_successful_bookings / total_capacity
    total_cancelled_bookings = len(fact_bookings[fact_bookings['booking_status'] == 'Cancelled'])
    cancellation_rate = total_cancelled_bookings / total_bookings
    
    return revenue_generated, total_bookings, average_rating, total_capacity, total_successful_bookings, occupancy_percentage, total_cancelled_bookings, cancellation_rate

# Main function
def main():
    base_path = 'C:/Users/LENOVO/Videos/Dataset'  # Update with your dataset folder path
    dim_date, dim_hotels, dim_rooms, fact_aggregated_bookings, fact_bookings = load_data(base_path)
    
    # Clean data
    dim_date, dim_hotels, dim_rooms, fact_aggregated_bookings, fact_bookings = clean_data(dim_date, dim_hotels, dim_rooms, fact_aggregated_bookings, fact_bookings)
    
    # Analyze metrics
    revenue_generated, total_bookings, average_rating, total_capacity, total_successful_bookings, occupancy_percentage, total_cancelled_bookings, cancellation_rate = analyze_metrics(fact_bookings, fact_aggregated_bookings)
    
    # Print results
    print("Metrics Visualization Placeholder")
    print(f"Revenue: ₹{revenue_generated}")
    print(f"Total Bookings: {total_bookings}")
    print(f"Average Rating: {average_rating}")
    print(f"Total Capacity: {total_capacity}")
    print(f"Total Successful Bookings: {total_successful_bookings}")
    print(f"Occupancy %: {occupancy_percentage}")
    print(f"Total Cancelled Bookings: {total_cancelled_bookings}")
    print(f"Cancellation Rate: {cancellation_rate}")

if __name__ == "__main__":
    main()
