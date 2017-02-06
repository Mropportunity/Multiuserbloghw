
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month(months):
     if months:
          short_month = months[:3].lower()
          return month_abbvs.get(short_month)