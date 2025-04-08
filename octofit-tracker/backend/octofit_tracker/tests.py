from django.test import TestCase
from bson import ObjectId
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(_id=ObjectId(), email="test@example.com", username="Test User", password="password123")
        self.assertEqual(user.email, "test@example.com")


class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(_id=ObjectId(), email="test@example.com", username="Test User", password="password123")
        team = Team.objects.create(_id=ObjectId(), name="Test Team")
        team.members.add(user)
        self.assertEqual(team.name, "Test Team")


class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(_id=ObjectId(), email="test@example.com", username="Test User", password="password123")
        activity = Activity.objects.create(_id=ObjectId(), user=user, activity_type="Running", duration="00:30:00")
        self.assertEqual(activity.activity_type, "Running")


class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create(_id=ObjectId(), email="test@example.com", username="Test User", password="password123")
        leaderboard = Leaderboard.objects.create(_id=ObjectId(), user=user, score=100)
        self.assertEqual(leaderboard.score, 100)


class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(_id=ObjectId(), name="Test Workout", description="A test workout")
        self.assertEqual(workout.name, "Test Workout")
