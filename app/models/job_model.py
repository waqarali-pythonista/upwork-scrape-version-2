from app import db

class Job(db.Model):
    """
    Job model to represent job details scraped from external sources.
    """
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    post_time = db.Column(db.String(100), nullable=True)
    location = db.Column(db.String(200), nullable=True)
    clock_hourly = db.Column(db.String(100), nullable=True)
    duration = db.Column(db.String(100), nullable=True)
    experience_level = db.Column(db.String(100), nullable=True)
    clock_timelog = db.Column(db.String(100), nullable=True)
    local = db.Column(db.String(100), nullable=True)
    project_type = db.Column(db.String(100), nullable=True)
    client_contract_date = db.Column(db.String(200), nullable=True)
    client_location = db.Column(db.String(200), nullable=True)
    client_spend = db.Column(db.String(200), nullable=True)
    client_hires = db.Column(db.String(200), nullable=True)
    client_hours = db.Column(db.String(200), nullable=True)
    client_company_profile = db.Column(db.Text, nullable=True)

    def __init__(self, job_title, description, post_time=None, location=None,
                 clock_hourly=None, duration=None, experience_level=None, clock_timelog=None,
                 local=None, project_type=None, client_contract_date=None, client_location=None,
                 client_spend=None, client_hires=None, client_hours=None, client_company_profile=None):
        self.job_title = job_title
        self.description = description
        self.post_time = post_time
        self.location = location
        self.clock_hourly = clock_hourly
        self.duration = duration
        self.experience_level = experience_level
        self.clock_timelog = clock_timelog
        self.local = local
        self.project_type = project_type
        self.client_contract_date = client_contract_date
        self.client_location = client_location
        self.client_spend = client_spend
        self.client_hires = client_hires
        self.client_hours = client_hours
        self.client_company_profile = client_company_profile

    def to_dict(self):
        """
        Converts the Job object to a dictionary for JSON serialization.
        """
        return {
            "id": self.id,
            "job_title": self.job_title,
            "description": self.description,
            "post_time": self.post_time,
            "location": self.location,
            "clock_hourly": self.clock_hourly,
            "duration": self.duration,
            "experience_level": self.experience_level,
            "clock_timelog": self.clock_timelog,
            "local": self.local,
            "project_type": self.project_type,
            "client_contract_date": self.client_contract_date,
            "client_location": self.client_location,
            "client_spend": self.client_spend,
            "client_hires": self.client_hires,
            "client_hours": self.client_hours,
            "client_company_profile": self.client_company_profile
        }
