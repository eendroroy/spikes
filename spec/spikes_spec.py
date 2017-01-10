import spikes

with description("spikes"):

    with it('should return bar-chart ->u\'\u2588\n\u2588\n\u2588\'<-'):
        assert spikes.spike([.1, ], 3) == u'\u2588\n\u2588\n\u2588'

    with it('should return bar-chart ->u\'\u2588\n\u2588\'<-'):
        assert spikes.spike([.1, ], 2) == u'\u2588\n\u2588'
        assert spikes.spike([.1, ]) == u'\u2588'

    with it('should return bar-chart ->u\'\u2588\'<-'):
        assert spikes.spike([.1, ], 1) == u'\u2588'

    with it('should return bar-chart ->\'\'<-'):
        assert spikes.spike([.1, ], 0) == ''

    with it('should return bar-chart ->u\'  \u2588\n \u2588\u2588\n\u2588\u2588\u2588\'<-'):
        assert spikes.spike([1, 2, 3], rows=3) == u'  \u2588\n \u2588\u2588\n\u2588\u2588\u2588'

    with it('should return bar-chart ->u\' \u2583\u2588\n\u2585\u2588\u2588\'<-'):
        assert spikes.spike([1, 2, 3], rows=2) == u' \u2583\u2588\n\u2585\u2588\u2588'

    with it('should return bar-chart ->u\'\u2583\u2585\u2588\'<-'):
        assert spikes.spike([1, 2, 3], rows=1) == u'\u2583\u2585\u2588'

    with it('should return bar-chart -><-'):
        assert spikes.spike([1, 2, 3], rows=0) == ''

    with it('should return bar-chart ->u\'\u2581\u2582\u2583\u2584\u2585\u2586\u2587\u2588\'<-'):
        assert spikes.spike([.1, .2, .3, .4, .5, .6, .7, .8]) == u'\u2581\u2582\u2583\u2584\u2585\u2586\u2587\u2588'

    with it('should return bar-chart ->u\'\u2581\u2582\u2583\u2584\u2585\u2586\u2587\u2588\'<-'):
        assert spikes.spike([1, 2, 3, 4, 5, 6, 7, 8]) == u'\u2581\u2582\u2583\u2584\u2585\u2586\u2587\u2588'
