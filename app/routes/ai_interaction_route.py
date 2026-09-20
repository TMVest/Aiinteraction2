from flask import Blueprint, render_template, redirect, url_for, flash,abort, request

def ai_interaction(ai_service):
    bp = Blueprint("ai", __name__, url_prefix="/ai")

    @bp.rout("/", methods=["GET"])
    def list_models():
        return models