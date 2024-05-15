#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The classic Tetris developed using PyGame.
    Copyright (C) 2018 Recursos Python - recursospython.com.
"""

from collections import OrderedDict
import random

from pygame import Rect
import pygame
import numpy as np


WINDOW_WIDTH, WINDOW_HEIGHT = 500, 601
GRID_WIDTH, GRID_HEIGHT = 300, 600
TILE_SIZE = 30


def remove_empty_columns(arr, _x_offset=0, _keep_counting=True):
    """
    Remove empty columns from arr (i.e. those filled with zeros).
    The return value is (new_arr, x_offset), where x_offset is how
    much the x coordinate needs to be increased in order to maintain
    the block's original position.
    """
    for colid, col in enumerate(arr.T):
        if col.max() == 0:
            if _keep_counting:
                _x_offset += 1
            # Remove the current column and try again.
            arr, _x_offset = remove_empty_columns(
                np.delete(arr, colid, 1), _x_offset, _keep_counting)
            break
        else:
            _keep_counting = False
    return arr, _x_offset

class BottomReached(Exception):
    pass

class TopReached(Exception):
    pass

class Block(pygame.sprite.Sprite):
    
    @staticmethod
    def collide(block, group):
        """
        Check if the specified block collides with some other block
        in the group.
        """

        for other_block in group:
            # Ignore the current block which will always collide with itself.
            if block == other_block:
                continue
            if pygame.sprite.collide_mask(block, other_block) is not None:
                return True
        return False
    
    def __init__(self):
        super().__init__()
        # Get a random color.
        self.color = random.choice((
            (200, 200, 200),
            (215, 133, 133),
            (30, 145, 255),
            (0, 170, 0),
            (180, 0, 140),
            (200, 200, 0)
        ))

        self.current = True

        self.struct = np.array(self.struct)
        # Initial random rotation and flip.
        if random.randint(0, 1):
            self.struct = np.rot90(self.struct)
        if random.randint(0, 1):
            # Flip in the X axis.
            self.struct = np.flip(self.struct, 0)
        self._draw()
    
    def _draw(self, x=4, y=0):
        width = len(self.struct[0]) * TILE_SIZE
        height = len(self.struct) * TILE_SIZE
        self.image = pygame.surface.Surface([width, height])
        self.image.set_colorkey((0, 0, 0))
        # Position and size
        self.rect = Rect(0, 0, width, height)
        self.x = x
        self.y = y
        for y, row in enumerate(self.struct):
            for x, col in enumerate(row):
                if col:
                    pygame.draw.rect(
                        self.image,
                        self.color,
                        Rect(x*TILE_SIZE + 1, y*TILE_SIZE + 1,
                             TILE_SIZE - 2, TILE_SIZE - 2)
                    )
        self._create_mask()

    def redraw(self):
        self._draw(self.x, self.y)

    def _create_mask(self):
        """
        Create the mask attribute from the main surface.
        The mask is required to check collisions. This should be called
        after the surface is created or update.
        """
        self.mask = pygame.mask.from_surface(self.image)

    def initial_draw(self):
        raise NotImplementedError
    
    @property
    def group(self):
        return self.groups()[0]
    
    @property
    def x (self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
        self.rect.left = value*TILE_SIZE

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y =value
        self.react.top = value*TILE_SIZE

    def move_left(self, group):
        self.x -= 1
        # Check if we reached the left margin
        if self.x < 0 or Block.collide (self, group):
            self.x =+ 1
    
    def move_right(self, group):
        self.x =+ 1
        #Check if we reached the right margin or collide with another
        #block
        if self.rect.right > GRID_WIDTH or Block.collide (self, group):
            #Rollback.
            self.x -= 1
    
    def rotate (self, group):
        self.image = pygame.transform.rotate (self.image, 90)
        # once rotate we need to update the size and position.
        self.rect.widht = self.image.get_widht()
        self.rect.height = self.image.get_height()
        self._create_mask()
        #Check the new position doesn't exceed the limits or collide
        # with other blocks and adjuat it if necessary.
        