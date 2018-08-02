import os


def read_metrics():

    root_path = os.path.dirname(os.path.abspath(__file__))[:-5]
    metrics_path = os.path.join(root_path, "files\\metrics.txt")

    with open(metrics_path, "r") as f_metrics:

        metrics = f_metrics.read()

    metric_list = metrics.split()
    print(metric_list)

    return metric_list