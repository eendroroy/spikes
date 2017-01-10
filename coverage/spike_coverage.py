import sys
from io import StringIO

from spikes.spike import spike

sys.stdin = StringIO()
sys.stderr = StringIO()

spike([1, 2, 3, 4, 5, 6, 7, 8], 0)
spike([1, 2, 3, 4, 5, 6, 7, 8], 1)
spike([1, 2, 3, 4, 5, 6, 7, 8], 2)
spike([1, 2, 3, 4, 5, 6, 7, 8], 3)

spike([1, 0, 3, 23, 45, 2, 1, 4, 56], 0)
spike([1, 0, 3, 23, 45, 2, 1, 4, 56], 1)
spike([1, 0, 3, 23, 45, 2, 1, 4, 56], 2)
spike([1, 0, 3, 23, 45, 2, 1, 4, 56], 3)

spike([0, 0, 0, 0], 2)
spike(['1', '2'], 2)
spike(['q'])
