# analyze_ss_movingload.py

def analyze_beam(L, t1, t2, x, a, eval_x=None):
    """
    Function to analyze a simply supported beam with two point loads.
    
    Parameters:
    L      : Total span of the beam
    t1     : First point load (W1)
    t2     : Second point load (W2)
    x      : Distance between the two loads
    a      : Distance from point A to the first load
    eval_x : Point on beam to evaluate SF and BM (optional)
    
    Output:
    Prints:
        - Reaction at A and B
        - Shear Force and Bending Moment at eval_x (BM_01, SF_01)
        - Maximum Shear Force (SF_max)
        - Maximum Bending Moment (BM_max)
    """

    W1 = t1
    W2 = t2

    # Positions of loads from A
    z1 = a
    z2 = a + x

    # Validate positions
    if z2 > L:
        print(" Error: Load positions exceed beam length.")
        return

    #  Step 1: Take Moment about A to find RB
    RB = (W1 * z1 + W2 * z2) / L

    #  Step 2: Use vertical equilibrium to find RA
    RA = W1 + W2 - RB

    # Set default eval point if not provided (use midspan)
    if eval_x is None:
        eval_x = L / 2

    #  Step 3: Shear Force at eval_x
    SF_01 = RA
    if z1 < eval_x:
        SF_01 -= W1
    if z2 < eval_x:
        SF_01 -= W2

    # Step 4: Bending Moment at eval_x
    BM_01 = RA * eval_x
    if z1 < eval_x:
        BM_01 -= W1 * (eval_x - z1)
    if z2 < eval_x:
        BM_01 -= W2 * (eval_x - z2)

    #  Max values
    SF_max = max(abs(RA), abs(RB))
    BM_max = max(
        abs(RA * z1),
        abs(RA * z2 - W1 * (z2 - z1)),
        abs(BM_01)
    )

    # Output
    print("\nBeam Analysis Results")
    print(f"Beam Length (L): {L} m")
    print(f"Load W1 = {W1} kN at a = {a} m from A")
    print(f"Load W2 = {W2} kN at a + x = {z2} m from A")
    print(f"Evaluation point: x = {eval_x} m\n")

    print(f" Maximum Reaction at A (RA): {RA:.2f} kN")
    print(f" Maximum Reaction at B (RB): {RB:.2f} kN")
    print(f" Shear Force at x = {eval_x} m (SF_01): {SF_01:.2f} kN")
    print(f" Bending Moment at x = {eval_x} m (BM_01): {BM_01:.2f} kNm")
    print(f" Maximum Shear Force (SF_max): {SF_max:.2f} kN")
    print(f" Maximum Bending Moment (BM_max): {BM_max:.2f} kNm")


# Example use case
if __name__ == "__main__":
    print("=== Simply Supported Beam Analysis ===")
    try:
        L = float(input("Enter beam length L (m): "))
        t1 = float(input("Enter load W1 (kN): "))
        t2 = float(input("Enter load W2 (kN): "))
        x = float(input("Enter distance between W1 and W2 (x) (m): "))
        a = float(input("Enter distance from A to W1 (a) (m): "))
        eval_x = float(input("Enter point x to evaluate SF and BM (m): "))

        analyze_beam(L, t1, t2, x, a, eval_x)

    except ValueError:
        print(" Invalid input. Please enter numeric values.")
