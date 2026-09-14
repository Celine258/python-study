import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import Game_stats
from button import Button
from socreboard import ScoreBoard
#############################################################################################################################
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))#创建一个显示窗口
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()#控制帧数
        self.bg_color = self.settings.bg_color#Red,Green,Blue三个颜色的参数
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.stats = Game_stats(self)
        self.game_active = True
        self.button = Button(self,"play")
        #self.game_score = 0
        #self.sb = ScoreBoard(self)
        
#############################################################################################################################
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
#############################################################################################################################

    def _check_play_button(self,mouse_pos):
        button_check = self.button.rect.collidepoint(mouse_pos)
        if button_check and not self.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.game_active = True
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom > self.settings.screen_height:
                self._ship_hit()
                break

    def _check_fleet_edge(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y +=self.settings.aline_drop_speed
        self.settings.fleet_direction *= -1    ###向下移动并且改变方向

    def _update_aliens(self):
        self._check_fleet_edge()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height= alien.rect.size

        current_x, current_y = alien_width,alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x,current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2* alien_height

    def _create_alien(self,current_x,current_y):
            new_alien = Alien(self)
            new_alien.x = current_x
            new_alien.rect.x = current_x
            new_alien.rect.y = current_y
            self.aliens.add(new_alien)
#############################################################################################################################

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        #以下为检测碰撞函数，其会判断两者是否重叠
        collision = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)#第一个为true即两者碰撞子弹会消失，第二个同理
        if not self.aliens:
            self.bullets.empty()
            self.settings.increse_speed()
            self._create_fleet()        
#############################################################################################################################

    def _check_event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit#点击右上角的叉叉即为退出
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_event(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_cvent(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_keydown_event(self,event):
        if event.key == pygame.K_RIGHT:
           self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
           self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_cvent(self,event):  
        if event.key == pygame.K_RIGHT:
           self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
           self.ship.moving_left = False

#############################################################################################################################
    def _update_screen(self):
        self.screen.fill(self.bg_color)#每次循环都重绘屏幕
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()#绘制子弹
        self.ship.blitme()#将飞船绘制到屏幕上
        self.aliens.draw(self.screen)#绘制外星人
        #self.sb.draw_score()
        if not self.game_active:
            self.button.draw_button()
        pygame.display.flip()#每次执行一个while循环时，使新的屏幕显示，旧的屏幕不显示，使动画更加连续
        self.clock.tick(60)#设置为60帧

#############################################################################################################################
    def run_game(self):
        while True:#每次循环更新屏幕
            self._check_event()
            self.ship.update()
            if self.game_active:
                self._update_bullets()
                self._update_aliens()
                self._update_screen()
            self.clock.tick(60)#设置为60帧
#############################################################################################################################
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


