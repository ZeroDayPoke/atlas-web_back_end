#!/usr/bin/env python3
"""Unittests for client.py"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """test class for GithubOrgClient"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        mock_org = {"name": org_name}
        mock_get_json.return_value = mock_org

        github_org_client = GithubOrgClient(org_name)
        self.assertEqual(github_org_client.org, mock_org)

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url."""
        mock_payload = {'repos_url': 'https://api.github.com/orgs/org/repos'}
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = mock_payload
            github_org_client = GithubOrgClient('org')
            self.assertEqual(github_org_client._public_repos_url, 'https://api.github.com/orgs/org/repos')
