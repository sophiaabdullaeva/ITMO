package info.attacks.statusmoves;
import ru.ifmo.se.pokemon.*;
public class Charm extends StatusMove {
    public Charm() {
        super(Type.FAIRY, 0, 100);
    }
    @Override
    protected boolean checkAccuracy(Pokemon att, Pokemon def) {
        return true;
    }
    //Понижает Атаку цели на две ступени.
    @Override
    protected void applyOppEffects(Pokemon pok) {
        pok.setMod(Stat.ATTACK, -2);
    }
    @Override
    protected String describe() {
        return "использует атаку Charm";
    }
}
