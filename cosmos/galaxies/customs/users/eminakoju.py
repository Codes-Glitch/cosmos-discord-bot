"""
Cosmos: A General purpose Discord bot.
Copyright (C) 2020 thec0sm0s

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from ... import Cog


class EminaKoju(Cog):

    __USER_ID = 394407882675978253

    @Cog.group(name="summon")
    @Cog.checks.check_user(__USER_ID)
    async def summon(self, ctx):
        pass

    @summon.command(name="mlbb", aliases=["ml", "MLBB"])
    async def summon_mlbb(self, ctx):
        to_summon = [
            331793750273687553, 250900865446182922, 463202259149258764, 332491715376054274, 517301933682327573,
            377756783130968064, 431890861278887947, 164676584756740096, 239099656330674178,
        ]
        content = " ".join([f"<@{user_id}>" for user_id in to_summon])
        await ctx.send(content)
