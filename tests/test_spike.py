import unittest

from spikes.spike import spike


class SpikeTest(unittest.TestCase):
    def test_bar_chart_1(self):
        """
        should return bar-chart ->u'\u2588\n\u2588\n\u2588'<-
        """
        self.assertEqual(
            spike([.1, ], 3),
            u'\u2588\n\u2588\n\u2588'
        )

    def test_bar_chart_2(self):
        """
        should return bar-chart ->u'\u2588\n\u2588\n\u2588'<-
        """
        self.assertEqual(
            spike([.1, ], 2),
            u'\u2588\n\u2588'
        )

    def test_bar_chart_3(self):
        """
        should return bar-chart ->u'\u2588'<-
        """
        self.assertEqual(
            spike([.1, ], 1),
            u'\u2588'
        )

    def test_bar_chart_4(self):
        """
        should return bar-chart ->u'  \u2588\n \u2588\u2588\n\u2588\u2588\u2588'<-
        """
        self.assertEqual(
            spike([1, 2, 3], rows=3),
            u'  \u2588\n \u2588\u2588\n\u2588\u2588\u2588'
        )

    def test_bar_chart_5(self):
        """
        should return bar-chart ->u' \u2583\u2588\n\u2585\u2588\u2588'<-
        """
        self.assertEqual(
            spike([1, 2, 3], rows=2),
            u' \u2583\u2588\n\u2585\u2588\u2588'
        )

    def test_bar_chart_6(self):
        """
        should return bar-chart ->u'\u2583\u2585\u2588'<-
        """
        self.assertEqual(
            spike([1, 2, 3], rows=1),
            u'\u2583\u2585\u2588'
        )

    def test_bar_chart_7(self):
        """
        should return bar-chart ->u'\u2581\u2582\u2583\u2584\u2585\u2586\u2587\u2588'<-
        """
        self.assertEqual(
            spike([.1, .2, .3, .4, .5, .6, .7, .8]),
            u'\u2581\u2582\u2583\u2584\u2585\u2586\u2587\u2588'
        )

    def test_bar_chart_8(self):
        """
        should return bar-chart ->u'\u2581\u2582\u2583\u2584\u2585\u2586\u2587\u2588'<-
        """
        self.assertEqual(
            spike([1, 2, 3, 4, 5, 6, 7, 8]),
            u'\u2581\u2582\u2583\u2584\u2585\u2586\u2587\u2588'
        )
