import sys, json
from backend.tasks.generate import generate_image_task

def main(prompts):
    if not prompts:
        print("No prompts provided", file=sys.stderr)
        sys.exit(2)
    results = []
    for p in prompts:
        asyncres = generate_image_task.delay(p)
        results.append({"prompt": p, "task_id": asyncres.id})
    print(json.dumps({"queued": results}, indent=2))

if __name__ == "__main__":
    main(sys.argv[1:])