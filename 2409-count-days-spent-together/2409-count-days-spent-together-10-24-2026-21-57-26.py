class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_days(date_str: str) -> int:
            month, day = map(int, date_str.split('-'))
            total_days = day
            for m in range(month - 1):
                total_days += days_in_months[m]
            return total_days
        
        alice_arrive = date_to_days(arriveAlice)
        alice_leave = date_to_days(leaveAlice)
        bob_arrive = date_to_days(arriveBob)
        bob_leave = date_to_days(leaveBob)
        
        start_overlap = max(alice_arrive, bob_arrive)
        end_overlap = min(alice_leave, bob_leave)
        
        return max(0, end_overlap - start_overlap + 1)