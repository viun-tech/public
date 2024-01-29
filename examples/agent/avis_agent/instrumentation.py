from vue_instrumentation.core import get_meter, get_tracer

SERVICE_NAME = "avis_agent"

tracer = get_tracer(SERVICE_NAME)
meter = get_meter(SERVICE_NAME)

total_run_duration_histogram = meter.create_histogram(
    name="agent.run_duration",
    unit="ms",
    description="measures the duration of running the agent",
)
cycle_counter = meter.create_up_down_counter(
    name="agent.cycles",
    description="The number of cycles the agent has run",
    unit="1",
)
write_signal_duration_histogram = meter.create_histogram(
    name="agent.signal.write_duration",
    unit="ms",
    description="measures the duration of writing to the signal interface",
)
backend_execute_duration_histogram = meter.create_histogram(
    name="agent.backend.execute_duration",
    unit="ms",
    description="measures the duration of executing a command on the backend",
)
capture_image_duration_histogram = meter.create_histogram(
    name="agent.camera.capture_duration",
    unit="ms",
    description="measures the duration of capturing an image",
)
heartbeat_metric = meter.create_counter(
    "agent.heartbeat",
    description="Heartbeat metric to check if the agent is running",
    unit="1",
)
image_sharpness_gauge = meter.create_observable_gauge(
    "agent.camera.image_sharpness",
    description="measures the sharpness of the captured image",
    unit="1",
)
image_brightness_gauge = meter.create_observable_gauge(
    "agent.camera.image_brightness",
    description="measures the brightness of the captured image",
    unit="1",
)
