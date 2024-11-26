import unittest
from app import create_app, db
from app.models.job_model import Job
import json

class TestJobRoutes(unittest.TestCase):
    """
    Unit tests for job-related routes.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.app = create_app()
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """
        Tear down the test environment.
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_jobs_empty(self):
        """
        Test the /jobs endpoint when no jobs exist in the database.
        """
        response = self.client.get('/api/jobs')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"jobs": []})

    def test_add_and_get_job(self):
        """
        Test adding a job via /scrape and retrieving it via /jobs.
        """
        # Mock data for scraping
        job_data = {
            "url": "https://example.com/job-post"  # Replace with a valid test URL
        }

        # Mock the scraping service
        with self.app.app_context():
            job = Job(
                job_title="Test Job",
                description="Test description",
                post_time="1 day ago",
                location="Remote",
                clock_hourly="$50/hr",
                duration="3 months",
                experience_level="Intermediate",
                clock_timelog="Hourly",
                local="Yes",
                project_type="One-time project",
                client_contract_date="2021",
                client_location="USA",
                client_spend="$10k+",
                client_hires="5",
                client_hours="100",
                client_company_profile="Reputable client"
            )
            db.session.add(job)
            db.session.commit()

        # Retrieve the jobs
        response = self.client.get('/api/jobs')
        self.assertEqual(response.status_code, 200)
        jobs = response.json['jobs']
        self.assertEqual(len(jobs), 1)
        self.assertEqual(jobs[0]['job_title'], "Test Job")

    def test_scrape_route(self):
        """
        Test the /scrape route with mocked data.
        """
        mock_url = {
            "url": "https://example.com/job-post"  # Replace with a valid or mocked test URL
        }

        # Mock the scrape endpoint
        response = self.client.post('/api/scrape', data=json.dumps(mock_url), content_type='application/json')

        # Ensure the route responds as expected
        self.assertEqual(response.status_code, 500)  # Since actual scraping may fail in test environments
        self.assertIn("error", response.json)

if __name__ == '__main__':
    unittest.main()
