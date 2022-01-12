import discord
from discord.ext import commands
import random
import helper

class connect_4(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.board = []
        self.gameOn = False
        self.player1 = ""
        self.player2 = ""
        self.turn = ""
        self.count = 0
    
    @commands.command()
    async def c4(self,ctx, p1: discord.Member):
        self.player1 = p1 
        board = [] 
        self.player2 = ctx.author
        if self.player1 == self.player2:
            await ctx.send(f'You cannot play connect 4 with yourself')
        elif self.player1.bot:
            await ctx.send(f'You cannot play with a bot')
        else:
            self.gameOn = True
            self.turn = p1


            self.board = [[":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:"],
                [":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:"],
                [":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:"],
                [":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:"],
                [":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:"],
                [":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:"]
            ]
            
            await ctx.send(f'{self.player1.mention} It is your turn.')
            line = helper.print_board(self.board)
            myembed =  discord.Embed(title = 'Connect 4', description = line,color =808080)
            msg = await ctx.send(embed = myembed)
    
    @commands.command()
    async def move(self,ctx,message = 'test'):
        #checks if there is a game being played already
        if self.gameOn == False:
            await ctx.send('there is no game right now')
        #checks if person making move is even playing
        elif ctx.author != self.player1 and ctx.author != self.player2:
            await ctx.send(f'You are not in this game')
        elif ctx.author != self.turn:
        #checks if its the right persons turn
            await ctx.send(f'It is not your turn')
        else:
            #checks if person didnt enter an number
            if message == 'test':
                await ctx.send('Make a move')
            #checking to see if number is out of range
            elif int(message) > 7 or int(message) < 1:
               await ctx.send('out of range')
            else:
                move = int(message) - 1
                i = 0
                j = -1
                #loops throw column to see if there is space
                for i in range(6):
                    if self.board[i][move] == ':white_circle:':
                        j = i
                #if j isnt -1 then column is not full
                if j != -1:
                    #checks if move is made by player one and if so it places a yellow circle
                    if self.player1 == self.turn:
                        self.board[j][move] = ':yellow_circle:'
                        line = helper.print_board(self.board)
                        myembed =  discord.Embed(title = 'Connect 4', description = line,color =808080)
                        #displays the board
                        await ctx.send(embed = myembed)
                        self.turn = self.player2
                        #chekcs if player has won the game
                        win = helper.has_won(self.board,move,j,':yellow_circle:')
                        self.count += 1
                        if win == True:
                            await ctx.send(f'{self.player1.mention} has won')
                            self.gameOn = False
                        elif self.count == 42:
                            self.gameOn = False
                            await ctx.send(f'Tie Game')

                    #checks if move is made by player two and if so it places a red circle
                    elif self.player2 == self.turn:
                        self.board[j][move] = ":red_circle:"
                        line = helper.print_board(self.board)
                        myembed =  discord.Embed(title = 'Connect 4', description = line,color =808080)
                        #displays the board
                        await ctx.send(embed = myembed)
                        self.turn = self.player1
                        win = helper.has_won(self.board,move,j,':red_circle:')
                        self.count += 1
                        if win == True:
                            await ctx.send(f'{self.player2.mention} has won')
                            self.gameOn = False
                        elif self.count == 42:
                                await ctx.send(f'Tie Game')
                                self.gameOn = False
                    else:
                        await ctx.send(f'That row is full pls try another move')
                        
                else:
                    await ctx.send('That row is full')
        

def setup(bot):
    bot.add_cog(connect_4(bot))