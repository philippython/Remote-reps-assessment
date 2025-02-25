# Ad Agency Budget Management System

## Overview
This project simulates budget management for an advertising agency handling multiple brands, each with daily and monthly budgets. It ensures that campaigns are turned off when budgets are exceeded and reactivated at the start of a new day or month. The system also respects dayparting schedules for campaigns.

## Features
- Tracks daily and monthly advertising spends per brand.
- Turns off campaigns when daily or monthly budgets are exceeded.
- Resets budgets and reactivates campaigns at the start of each day/month.
- Implements dayparting to control when campaigns can run.

## Data Structures
### Brand
- `name`: Brand name
- `daily_budget`: Maximum spend per day
- `monthly_budget`: Maximum spend per month
- `current_daily_spend`: Tracks daily spend
- `current_monthly_spend`: Tracks monthly spend
- `campaigns`: List of associated campaigns

### Campaign
- `name`: Campaign name
- `is_active`: Status of the campaign
- `spend_today`: Tracks daily spend per campaign
- `dayparting_hours`: List of active hours (e.g., `[(9, 17)]` for 9 AM to 5 PM)

### AdAgency
- Maintains a list of brands
- Handles daily and monthly resets

## Installation & Usage
1. Clone the repository:
   ```sh
   git clone <https://github.com/philippython/Remote-reps-assessment>
   ```
2. Run the script:
   ```sh
   python main.py
   ```

## Example Workflow
1. Create an `AdAgency` instance.
2. Add a `Brand` with defined budgets.
3. Attach `Campaigns` to the brand.
4. Simulate ad spend and observe how campaigns are managed based on budgets.

## Assumptions
- The system checks and updates budgets in real-time.
- Campaigns turn off when exceeding budgets and resume when permitted.
- Dayparting ensures campaigns only run within specified hours.

