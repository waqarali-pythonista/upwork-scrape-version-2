from flask import Blueprint, request, jsonify
from app.models.job_model import Job
from app import db
from app.services.scraping_service import ScrapingService

# Define the Blueprint for job-related routes
job_bp = Blueprint('job', __name__)

@job_bp.route('/', methods=['GET'])
def welcome():
    """
    Root route that returns a welcome message.
    """
    return jsonify({"message": "Welcome to Muscled App"}), 200

@job_bp.route('/scrape', methods=['POST'])
def scrape_job():
    """
    Route to scrape job details from a given URL.
    Expects a JSON payload with a "url" field.
    """
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        # Scrape job details using the ScrapingService
        job_data = ScrapingService.scrape_job_details(url)

        # Save job details to the database
        job = Job(
            job_title=job_data.get('job_title'),
            description=job_data.get('description'),
            post_time=job_data.get('post_time'),
            location=job_data.get('location'),
            clock_hourly=job_data.get('clock_hourly'),
            duration=job_data.get('duration'),
            experience_level=job_data.get('experience_level'),
            clock_timelog=job_data.get('clock_timelog'),
            local=job_data.get('local'),
            project_type=job_data.get('project_type'),
            client_contract_date=job_data.get('client_contract_date'),
            client_location=job_data.get('client_location'),
            client_spend=job_data.get('client_spend'),
            client_hires=job_data.get('client_hires'),
            client_hours=job_data.get('client_hours'),
            client_company_profile=job_data.get('client_company_profile'),
        )
        db.session.add(job)
        db.session.commit()

        # Return the scraped job details as JSON
        return jsonify({
            "message": "Job details successfully scraped and saved.",
            "job": {
                "id": job.id,
                "job_title": job.job_title,
                "description": job.description,
                "post_time": job.post_time,
                "location": job.location,
                "clock_hourly": job.clock_hourly,
                "duration": job.duration,
                "experience_level": job.experience_level,
                "clock_timelog": job.clock_timelog,
                "local": job.local,
                "project_type": job.project_type,
                "client_contract_date": job.client_contract_date,
                "client_location": job.client_location,
                "client_spend": job.client_spend,
                "client_hires": job.client_hires,
                "client_hours": job.client_hours,
                "client_company_profile": job.client_company_profile,
            }
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@job_bp.route('/jobs', methods=['GET'])
def get_jobs():
    """
    Route to retrieve all jobs from the database.
    Returns a list of jobs in JSON format.
    """
    try:
        jobs = Job.query.all()
        jobs_data = [
            {
                "id": job.id,
                "job_title": job.job_title,
                "description": job.description,
                "post_time": job.post_time,
                "location": job.location,
                "clock_hourly": job.clock_hourly,
                "duration": job.duration,
                "experience_level": job.experience_level,
                "clock_timelog": job.clock_timelog,
                "local": job.local,
                "project_type": job.project_type,
                "client_contract_date": job.client_contract_date,
                "client_location": job.client_location,
                "client_spend": job.client_spend,
                "client_hires": job.client_hires,
                "client_hours": job.client_hours,
                "client_company_profile": job.client_company_profile,
            }
            for job in jobs
        ]
        return jsonify({"jobs": jobs_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
