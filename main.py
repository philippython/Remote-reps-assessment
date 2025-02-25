from datetime import datetime, time

class Campaign:
    def __init__(self, name: str, dayparting_hours=None):
        self.name = name
        self.is_active = True
        self.spend_today = 0.0
        self.dayparting_hours = dayparting_hours or []  # List of (start_hour, end_hour)

    def can_run_now(self):
        if not self.dayparting_hours:
            return True
        
        current_hour = datetime.now().hour
        return any(start <= current_hour < end for start, end in self.dayparting_hours)

class Brand:
    def __init__(self, name: str, daily_budget: float, monthly_budget: float):
        self.name = name
        self.daily_budget = daily_budget
        self.monthly_budget = monthly_budget
        self.current_daily_spend = 0.0
        self.current_monthly_spend = 0.0
        self.campaigns = []

    def add_campaign(self, campaign: Campaign):
        self.campaigns.append(campaign)

    def update_spend(self, amount: float):
        self.current_daily_spend += amount
        self.current_monthly_spend += amount
        
        if self.current_daily_spend >= self.daily_budget or self.current_monthly_spend >= self.monthly_budget:
            self.disable_all_campaigns()
    
    def disable_all_campaigns(self):
        for campaign in self.campaigns:
            campaign.is_active = False

    def reset_daily_budget(self):
        self.current_daily_spend = 0.0
        self.enable_campaigns()
    
    def reset_monthly_budget(self):
        self.current_monthly_spend = 0.0
        self.enable_campaigns()

    def enable_campaigns(self):
        for campaign in self.campaigns:
            if campaign.can_run_now():
                campaign.is_active = True

class AdAgency:
    def __init__(self):
        self.brands = []

    def add_brand(self, brand):
        self.brands.append(brand)

    def process_daily_reset(self):
        for brand in self.brands:
            brand.reset_daily_budget()

    def process_monthly_reset(self):
        for brand in self.brands:
            brand.reset_monthly_budget()

# Example Usage
if __name__ == "__main__":
    agency = AdAgency()
    brand1 = Brand("Brand A", daily_budget=500, monthly_budget=10000)
    campaign1 = Campaign("Campaign 1", dayparting_hours=[(9, 17)])  # Runs from 9 AM to 5 PM
    campaign2 = Campaign("Campaign 2")  # Always active

    brand1.add_campaign(campaign1)
    brand1.add_campaign(campaign2)
    agency.add_brand(brand1)

    # Simulate Ad Spend
    brand1.update_spend(600)  # Exceeds daily budget, campaigns should stop
    print([(c.name, c.is_active) for c in brand1.campaigns])
