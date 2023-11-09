from redis import Redis
import rq


queue = rq.Queue('microblog-tasks', connection=Redis.from_url('redis://'))
job = queue.enqueue('app.tasks.example', 23)

job.get_id()

job.meta

job.refresh()
job.meta