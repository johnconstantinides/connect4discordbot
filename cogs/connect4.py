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
    
    @commands.command()
    async def c4(self,ctx, p1: discord.Member):
        self.player1 = p1 
        board = [] 
        self.player2 = ctx.author

        self.gameOn = True
        self.turn = p1

        if self.gameOn:

            self.board = [":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",
                ":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",
                ":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",
                ":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",
                ":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",
                ":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",":white_circle:",
            ]
            
            await ctx.send(f'{self.player1.mention} It is your turn.')
            line = helper.print_board(self.board)
            myembed =  discord.Embed(title = 'Connect 4', description = line,color =808080)
            msg = await ctx.send(embed = myembed)
    
    @commands.command()
    async def move(self,ctx,message = 'test'):
        if self.gameOn == False:
            await ctx.send('there is no game rn idiot')
        elif ctx.author != self.player1 and ctx.author != self.player2:
            await ctx.send(f'You are not in this game idiot')
        elif ctx.author != self.turn:
            await ctx.send(f'It is not your turn idiot')
        else:
            if message == 'test':
                await ctx.send('Make a move retard')
            elif int(message) > 7 or int(message) < 1:
               await ctx.send('out of range idiot')
            else:
                move = int(message) - 1
                i = 0
                j = -1
                for i in range(move,35+move+1,7):
                    if self.board[i] == ':white_circle:':
                        j = i
                if j != -1:
                    if self.player1 == self.turn:
                        self.board[j] = ':yellow_circle:'
                        line = helper.print_board(self.board)
                        myembed =  discord.Embed(title = 'Connect 4', description = line,color =808080)
                        await ctx.send(embed = myembed)
                        self.turn = self.player2
                        win = helper.has_won(self.board,j,':yellow_circle:')
                        if win == True:
                            await ctx.send(f'{self.player1.mention} has won')
                            self.gameOn = False
                        else:
                            print('cock')
                    elif self.player2 == self.turn:
                        self.board[j] = ":red_circle:"
                        line = helper.print_board(self.board)
                        myembed =  discord.Embed(title = 'Connect 4', description = line,color =808080)
                        await ctx.send(embed = myembed)
                        self.turn = self.player1
                        win = helper.has_won(self.board,j,':red_circle:')
                        if win == True:
                            await ctx.send(f'{self.player2.mention} has won')
                            self.gameOn = False
                    else:
                        await ctx.send(f'That row is full pls try another move')
                else:
                    await ctx.send('That row is full idiot')
        

def setup(bot):
    bot.add_cog(connect_4(bot))