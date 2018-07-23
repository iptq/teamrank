from .objects import db

class Tournament(db.Model):
	__tablename__ = "tournaments"
	id = db.Column(db.Integer, primary_key=True)
	owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
	teams = db.relationship("TournamentTeam", backref="tourn", lazy=True)

class TournamentTeam(db.Model):
	__tablename__ = "tournament_teams"
	id = db.Column(db.Integer, primary_key=True)
	tourn_id = db.Column(db.Integer, db.ForeignKey("tournaments.id"), nullable=False)
	name = db.Column(db.Unicode(256))

class Match(db.Model):
	__tablename__ = "matches"
	id = db.Column(db.Integer, primary_key=True)

players = db.Table("players",
	db.Column("team", db.Integer, db.ForeignKey("tournament_teams.id"), primary_key=True),
	db.Column("player", db.Integer, db.ForeignKey("users.osuid"), primary_key=True),
)

outcomes = db.Table("outcomes",
	db.Column("team1", db.Integer, db.ForeignKey("tournament_teams.id"), primary_key=True),
	db.Column("team2", db.Integer, db.ForeignKey("tournament_teams.id"), primary_key=True),
	db.Column("timestamp", db.DateTime, nullable=False),
	db.Column("score1", db.Integer, nullable=False),
	db.Column("score2", db.Integer, nullable=False),
	db.Column("mplink", db.String(256), nullable=True),
)

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	osuid = db.Column(db.Integer, unique=True, index=True)
	tournaments = db.relationship("Tournament", backref="owner", lazy=True)
