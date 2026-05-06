import unittest

from src.parity_tool_scan_flow.domain_review import DomainReview, review_lane, review_score


class DomainReviewTests(unittest.TestCase):
    def test_review_lane(self) -> None:
        item = DomainReview(59, 33, 29, 52)
        self.assertEqual(review_score(item), 116)
        self.assertEqual(review_lane(item), "watch")


if __name__ == "__main__":
    unittest.main()
