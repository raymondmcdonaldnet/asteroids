from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		# Already done with small asteroids.
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		# Larger asteroids need to spawn new asteroids on death.
		else:
			spawn_angle = random.uniform(20, 50)
			new_radius = self.radius - ASTEROID_MIN_RADIUS

			left_hand_asteroid_velocity = self.velocity.rotate(-spawn_angle) * 1.2
			left_hand_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
			left_hand_asteroid.velocity = left_hand_asteroid_velocity

			right_hand_asteroid_velocity = self.velocity.rotate(spawn_angle) * 1.2
			right_hand_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
			right_hand_asteroid.velocity = right_hand_asteroid_velocity
