import spikes

with description("spikes"):

    with it('should return bar-chart ->▁▂▃▄▅▆▇█<-'):
        assert spikes.spike([1, 2, 3, 4, 5, 6, 7, 8]) == "▁▂▃▄▅▆▇█"

    with it('should return bar-chart ->  █\n ██\n███<-'):
        assert spikes.spike([1, 2, 3], rows=3) == "  █\n ██\n███"

    with it('should return bar-chart -> ▃█\n▅██<-'):
        assert spikes.spike([1, 2, 3], rows=2) == " ▃█\n▅██"

    with it('should return bar-chart ->▃▅█<-'):
        assert spikes.spike([1, 2, 3], rows=1) == "▃▅█"

    with it('should return bar-chart -><-'):
        assert spikes.spike([1, 2, 3], rows=0) == ""
