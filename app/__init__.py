from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    # 'Slice' of SkillSync: public jobs feed (static for demo tests)
    @app.get("/jobs")
    def jobs():
        return jsonify([
            {"id": 1, "title": "Backend Developer", "company": "SkillSync", "location": "Remote"},
            {"id": 2, "title": "DevOps Engineer", "company": "CloudWorks", "location": "Detroit, MI"}
        ]), 200

    return app


app = create_app()