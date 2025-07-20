
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_price(request):
    token = request.GET.get("token")
    timestamp = int(request.GET.get("timestamp"))

    data = [
        {"timestamp": 1620000000, "price": 210},
        {"timestamp": 1620003600, "price": 215},
        {"timestamp": 1620007200, "price": 225},
    ]

    data = sorted(data, key=lambda x: x["timestamp"])
    times = [d["timestamp"] for d in data]
    prices = [d["price"] for d in data]

    if timestamp < times[0] or timestamp > times[-1]:
        return Response({"error": "Timestamp out of range"}, status=400)

    for i in range(len(times) - 1):
        if times[i] <= timestamp <= times[i + 1]:
            t1, p1 = times[i], prices[i]
            t2, p2 = times[i + 1], prices[i + 1]
            price = p1 + ((timestamp - t1) / (t2 - t1)) * (p2 - p1)
            return Response({
                "token": token,
                "timestamp": timestamp,
                "interpolated_price": round(price, 4)
            })

    return Response({"error": "Interpolation failed"}, status=500)
