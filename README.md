# Campus-tasks

## Démarrage

Projet utilisé dans les ateliers DevOps.

## Santé du service

Point prévu : GET /health

## Support
Contact: equipe-b@example.invalid
Contact : equipe-a@example.invalid

## Lancer la pile (Docker Compose)

- Démarrer : `docker compose up -d`
- Vérifier : `curl http://localhost:8089/health` (le port 8089 de l'hôte mène au port 8080 du conteneur)
- Base PostgreSQL : non publiée, accessible uniquement depuis le service `api`; données dans le volume `pgdata`
- Adminer (développement seulement) : `docker compose --profile debug up -d`, puis http://localhost:8081
- Ne jamais utiliser `docker compose down -v` sauf pour repartir de zéro (supprime les données)
